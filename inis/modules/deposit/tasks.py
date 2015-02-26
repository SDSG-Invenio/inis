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

from functools import wraps

from invenio.modules.deposit.models import Deposition


#
# Workflow tasks
#
def check_files():
    """Check if ttf and txt files look like TTF metadata."""
    @wraps(check_files)
    def _check_files(obj, eng):
        d = Deposition(obj)
        sip = d.get_latest_sip(sealed=False)
        if sip is None:
            sip = d.create_sip()
        # FIXME
        # f = open('/tmp/log', 'w')
        # f.write(str(sip.metadata['fft']) + '\n')
        # f.close()
        return False

    return _check_files


def reject():
    """Notify user that upload has failed."""
    @wraps(reject)
    def _reject(obj, eng):
        from invenio.modules.messages.query import create_message, send_message
        from invenio.config import CFG_SITE_URL
        d = Deposition(obj)
        sip = d.get_latest_sip(sealed=False)
        if sip is None:
            sip = d.create_sip()

        # FIXME
        # f = open('/tmp/log', 'aw')
        # f.write("dicc:\n" + str(sip.__dict__) + '\n\n')
        # f.close()
        dep_url = CFG_SITE_URL + '/deposit/upload/' + str(sip.metadata['owner']['deposition_id'])
        dep_link = "<a href=%(url)s>%(title)s</a>" % {'url': dep_url, 'title': sip.metadata['title.title']}

        rec_url = CFG_SITE_URL + '/record/' + str(sip.metadata['recid'])
        rec_link = "<a href=%(url)s>%(title)s</a>" % {'url': rec_url, 'title': sip.metadata['title.title']}

        msg = """Title: %(title)s</br>
                 Recid: %(rec_link)s</br>
                 Submission: %(dep_link)s</br>
                 Member: %(member)s
              """ % {'title': sip.metadata['title.title'], 'recid': sip.metadata['recid'],
                     'dep_link': dep_link, 'member': sip.metadata['member'][0],
                     'rec_link': rec_link}

        subject = 'Failed Submission #%s' % sip.metadata['owner']['deposition_id']
        # write_message(message)
        #(subject, body) = generate_msg(recid, [message])
        message_id = create_message(uid_from=1, users_to_str=sip.metadata['owner']['id'], msg_subject=subject, msg_body=msg)
        send_message(sip.metadata['owner']['id'], message_id)

    return _reject


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)


# def get_TRNs(recid):
#     TRNs = []
#     bibarchive = BibRecDocs(recid)
#     for name in bibarchive.get_bibdoc_names():
#         bibdoc = bibarchive.get_bibdoc(name)
#         for bibdocfile in bibdoc.list_latest_files():
#             if bibdocfile.format == '.ttf':
#                 f = open(bibdocfile.get_path(), 'r')
#                 ttf = f.read()
#                 f.close()
#                 TRNs += [ttf[i + 4:i + 13] for i in list(find_all(ttf, '001^'))]
#     return TRNs
