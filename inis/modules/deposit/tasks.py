# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2012, 2013, 2014 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""INIS workflow tasks."""
import os

from functools import wraps

from urllib2 import urlopen

from flask import current_app

from invenio.modules.deposit.models import Deposition


#
# Workflow tasks
#
def validate():
    """Check if ttf and txt files look like TTF metadata."""
    @wraps(validate)
    def _validate(obj, eng):
        d = Deposition(obj)
        sip = d.get_latest_sip(sealed=False)
        if sip is None:
            sip = d.create_sip()
        return sip.metadata['errors'] == []

    return _validate


def notify_rejection():
    """Notify user that upload has failed."""
    @wraps(notify_rejection)
    def _notify_rejection(obj, eng):
        from invenio.modules.messages.query import create_message, send_message
        from invenio.config import CFG_SITE_URL

        d = Deposition(obj)
        sip = d.get_latest_sip(sealed=False)
        if sip is None:
            sip = d.create_sip()

        dep_url = CFG_SITE_URL + '/deposit/upload/' + str(sip.metadata['owner']['deposition_id'])
        dep_link = "<a href=%(url)s>%(url)s</a>" % {'url': dep_url, 'title': sip.metadata['title.title']}

        rec_url = CFG_SITE_URL + '/record/' + str(sip.metadata['recid'])
        rec_link = "<a href=%(url)s>%(url)s</a>" % {'url': rec_url, 'title': sip.metadata['title.title']}

        try:
            member = sip.metadata['member']
        except IndexError:
            member = ''

        msg = """Title: %(title)s</br>
                 Submission: %(dep_link)s</br>
                 INIS Member: %(member)s</br></br>
                 Errors:</br>%(errors)s
              """ % {'title': sip.metadata['title.title'], 'recid': sip.metadata['recid'],
                     'dep_link': dep_link, 'member': member,
                     'rec_link': rec_link, 'errors': sip.metadata['error_message']}

        subject = 'Failed Submission #%s' % sip.metadata['owner']['deposition_id']
        # write_message(message)
        #(subject, body) = generate_msg(recid, [message])
        message_id = create_message(uid_from=1, users_to_str=sip.metadata['owner']['username'], msg_subject=subject, msg_body=msg)
        send_message(sip.metadata['owner']['id'], message_id)

    return _notify_rejection


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)


def get_TRNs(sip):
    TRNs = []
    change_records = []
    files = sip.metadata['fft']
    files_without_records = []
    for submitted_file in files:
        path = submitted_file['path']
        ext = os.path.splitext(path)[1]
        if ext in current_app.config['DEPOSIT_ACCEPTED_MD_EXTENSIONS']:
            f = open(path, 'r')
            ttf = f.read()
            f.close()
            records = [r.strip() for r in ttf.split('001^') if r.strip() != '']
            TRNs_this_file = []
            change_records_this_file = []
            for record in records:
                lines = [r.strip() for r in record.splitlines() if r.strip() != '']
                TRNs_this_file.append(lines[0])
                for l in lines:
                    if l.startswith('004^') and l[4] == 'C':
                        change_records_this_file.append(lines[0])

            # TRNs_this_file = [ttf[i + 4:i + 13] for i in list(find_all(ttf, '001^'))]
            # change_records_this_file = [ttf[i + 4:i + 13] for i in list(find_all(ttf, '004^'))]
            if len(TRNs_this_file) == 0:
                files_without_records.append(submitted_file['name'])
            TRNs += TRNs_this_file
            change_records += change_records_this_file

    sip.metadata['change_records'] = change_records
    sip.metadata['empty_md_files'] = files_without_records
    if files_without_records != []:
        sip.metadata['errors'].append({'code': 1, 'list': files_without_records})

    return TRNs


def trn_exists(trn):
    url = 'http://nkp.iaea.org/changerecord/inischangerecord.asmx/ProcRecords?list='
    try:
        response = urlopen(url + trn)
        html = response.read()
        return html.find('<string xmlns="http://nis.iaea.org/webservices/">1') > -1
    except e:
        return False


def file_names_not_in_TRNs(sip):
    from invenio.config import CFG_SITE_NAME
    from invenio.legacy.search_engine import perform_request_search

    files = sip.metadata['fft']
    TRNs = set(sip.metadata['trns'])
    names = set()
    for submitted_file in files:
        ext = os.path.splitext(submitted_file['path'])[1]
        if ext in current_app.config['DEPOSIT_ACCEPTED_FULLTEXT_EXTENSIONS']:
            names.add(submitted_file['name'])
    diff = list(names - TRNs)  # not in current upload
    missing = []
    for trn in diff:
        if perform_request_search(p=trn, cc=CFG_SITE_NAME, f='trn') == []:  # not in IIM
            if not trn_exists(trn):  # not in INIS DB
                missing.append(trn)

    return missing


def get_duplicated_trns(sip):
    TRNs = set(sip.metadata['trns'])
    change_records = set(sip.metadata['change_records'])
    duplicated_trns = []
    for trn in list(TRNs - change_records):
        if trn_exists(trn):
            duplicated_trns.append(trn)

    return duplicated_trns


def create_error_message(sip):
    from inis.config import CFG_SUMBISSION_ERRORS
    errors = "<ul>"
    for e in sip.metadata['errors']:
        errors += "<li>" + CFG_SUMBISSION_ERRORS[e['code']]
        if e['list']:
            errors += "<ul><li>%s</li></ul>" % '</li><li>'.join(e['list'])
        errors += "</li>"
    errors += "</ul>"
    return errors
