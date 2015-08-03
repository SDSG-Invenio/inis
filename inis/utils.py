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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

import string

from invenio.config import CFG_SITE_NAME, CFG_SITE_SECURE_URL, \
    CFG_SITE_SUPPORT_EMAIL, CFG_WEBSESSION_RESET_PASSWORD_EXPIRE_IN_DAYS


def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    import random
    return ''.join(random.choice(chars) for _ in range(size))


def tmpl_set_password_email_body(email, reset_key):
    """
    The body of the email that sends lost internal account
    passwords to users.
    """
    from invenio.utils.url import make_canonical_urlargd

    out = """
%(intro)s

%(intro2)s

<%(link)s>

%(outro)s

%(outro2)s""" % {
        'intro': "We have created an account for you at %(x_sitename)s (%(x_siteurl)s)\nfor "
                 "the account \"%(x_email)s\"." % {'x_sitename': CFG_SITE_NAME, 'x_siteurl': CFG_SITE_SECURE_URL, 'x_email': email},
        'intro2': "Please set your password following this link:",
        'link': "%s/youraccount/resetpassword%s" %
                (CFG_SITE_SECURE_URL, make_canonical_urlargd({
                    'ln': 'en',
                    'k': reset_key
                }, {})),
        'outro': "",
        'outro2': "Please note that this URL will remain valid for about %(days)s days only." %
                  {'days': CFG_WEBSESSION_RESET_PASSWORD_EXPIRE_IN_DAYS}
    }
    return out


def set_password(email):
    from invenio.ext.email import send_email
    from invenio.modules.access.mailcookie import mail_cookie_create_pw_reset
    from datetime import timedelta
    reset_key = mail_cookie_create_pw_reset(email, cookie_timeout=timedelta(days=CFG_WEBSESSION_RESET_PASSWORD_EXPIRE_IN_DAYS))
    send_email(CFG_SITE_SUPPORT_EMAIL, email,
               "%s %s" % ("Set your password for", CFG_SITE_NAME),
               tmpl_set_password_email_body(email, reset_key))


def create_user(name, email, country):
    from invenio.ext.sqlalchemy import db
    from invenio.modules.accounts.models import User, Usergroup, UserUsergroup
    from inis.config import CFG_MEMBERS_DICT

    u = User(email=email, nickname=name, password=id_generator())
    db.session.add(u)
    db.session.commit()

    ug = Usergroup.query.filter_by(name=CFG_MEMBERS_DICT[country]).first()
    ug.users.append(UserUsergroup(id_user=u.id))
    db.session.add(ug)
    db.session.commit()

    set_password(email)


def delete_record(recid):
    import os
    import tempfile
    from invenio.config import CFG_TMPDIR
    from invenio.legacy.bibrecord import record_add_field, record_xml_output
    from invenio.legacy.bibsched.bibtask import task_low_level_submission
    from invenio.legacy.search_engine import get_record

    r = get_record(recid)
    record_add_field(r, '980', subfields=[('c', 'DELETED')])

    fd, name = tempfile.mkstemp(suffix='.xml', prefix='deletion', dir=CFG_TMPDIR)

    os.write(fd, """<collection>\n""")
    os.write(fd, record_xml_output(r))
    os.write(fd, """</collection>\n""")
    os.close(fd)

    task_low_level_submission('bibupload', 'admin', '-i', '-r', name, '-P5')


def delete_submission(submission_id):
    from invenio.modules.deposit.models import Deposition

    depositions = Deposition.get_depositions()
    d = [e for e in depositions if e.id == submission_id]
    if d != []:
        d = d[0]
        s = d.get_latest_sip()
        recid = s.metadata['recid']
        d.delete()
        delete_record(recid)


def import_ttf(filename):

    import os
    import tempfile
    from invenio.config import CFG_TMPDIR
    from invenio.legacy.bibrecord import record_add_field, record_xml_output
    from invenio.legacy.bibsched.bibtask import task_low_level_submission

    separator = '001^'

    f = open(filename, 'r')
    raw_input = f.read()
    f.close()

    fd, name = tempfile.mkstemp(suffix='.xml', prefix='from_ttf', dir=CFG_TMPDIR)
    os.write(fd, """<collection>\n""")

    f = open('./inis/demosite/INIS_UCH.ai', 'r')
    a = f.read()
    b = [separator+e.strip() for e in a.split(separator) if e != ""]
    c = [(e.splitlines()[1].strip()[4:], e.splitlines()[0].strip()[4:]) for e in b]
    d = dict(c)

    for rule in d:
        raw_input = raw_input.replace(rule, unichr(int(d[rule].strip('#'), 16)).encode('utf-8'))

    raw_records = [separator+e.strip() for e in raw_input.split(separator) if e != ""]

    for raw_record in raw_records:
        r = {}
        ttf = dict([(l.split('^')[0], l.split('^')[1].strip()) for l in raw_record.splitlines()])
        for tag in ttf:
            value = ttf[tag].strip('(). \n\t')
            if tag == '001':  # trn
                record_add_field(r, '911', subfields=[('x', value)])
            elif tag in ['100']:  # authors
                for v in value.split(';'):
                    record_add_field(r, tag, subfields=[('a', v.strip())])
            elif tag == '800':  # keywords (descriptors)
                for v in value.split(';'):
                    record_add_field(r, '653', '1', subfields=[('a', v.strip())])
            elif tag == '200':  # title
                record_add_field(r, '245', subfields=[('a', value)])
            elif tag == '860':  # abstract
                record_add_field(r, '520', subfields=[('a', value)])
            else:
                record_add_field(r, tag, subfields=[('x', value)])

        record_add_field(r, '980', subfields=[('a', 'FROM_TTF')])
        os.write(fd, record_xml_output(r))

    os.write(fd, """\n</collection>\n""")
    os.close(fd)

    task_low_level_submission('bibupload', 'admin', '-i', name)
