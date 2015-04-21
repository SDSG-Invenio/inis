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
        'intro2': "Please set you password following this link:",
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
               "%s %s" % ("Set you password for", CFG_SITE_NAME),
               tmpl_set_password_email_body(email, reset_key))
