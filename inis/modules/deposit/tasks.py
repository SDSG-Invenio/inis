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

from invenio.legacy.search_engine import perform_request_search
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
        collections = sip.metadata['collections']
        for coll in collections:
            if coll['primary'] == 'Rejected':
                return False
        return True

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
        dep_link = "<a href=%(url)s>%(title)s</a>" % {'url': dep_url, 'title': sip.metadata['title.title']}

        rec_url = CFG_SITE_URL + '/record/' + str(sip.metadata['recid'])
        rec_link = "<a href=%(url)s>%(title)s</a>" % {'url': rec_url, 'title': sip.metadata['title.title']}

        try:
            member = sip.metadata['member'][0]
        except IndexError:
            member = ''

        msg = """Title: %(title)s</br>
                 Recid: %(rec_link)s</br>
                 Submission: %(dep_link)s</br>
                 Member: %(member)s
              """ % {'title': sip.metadata['title.title'], 'recid': sip.metadata['recid'],
                     'dep_link': dep_link, 'member': member,
                     'rec_link': rec_link}

        subject = 'Failed Submission #%s' % sip.metadata['owner']['deposition_id']
        # write_message(message)
        #(subject, body) = generate_msg(recid, [message])
        message_id = create_message(uid_from=1, users_to_str=sip.metadata['owner']['id'], msg_subject=subject, msg_body=msg)
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
    files = sip.metadata['fft']
    for submitted_file in files:
        path = submitted_file['path']
        ext = os.path.splitext(path)[1]
        if ext in current_app.config['DEPOSIT_ACCEPTED_MD_EXTENSIONS']:
            f = open(path, 'r')
            ttf = f.read()
            f.close()
            TRNs += [ttf[i + 4:i + 13] for i in list(find_all(ttf, '001^'))]
    return TRNs


def trn_exists(trn):
    url = 'http://nkp.iaea.org/changerecord/inischangerecord.asmx/ProcRecords?list='
    try:
        response = urlopen(url + trn)
        html = response.read()
        return html.find('<string xmlns="http://nis.iaea.org/webservices/">1') > -1
    except TypeError:
        return False


def file_names_not_in_TRNs(sip):
    from invenio.config import CFG_SITE_NAME

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
