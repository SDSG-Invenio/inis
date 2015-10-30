# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2012, 2013, 2014, 2015 CERN.
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
import sys

from flask import current_app

from inis.config import CFG_MONTH_CODES, CFG_SEASON_CODES

from invenio.config import CFG_SITE_NAME, CFG_SITE_SECURE_URL, \
    CFG_SITE_SUPPORT_EMAIL, CFG_WEBSESSION_RESET_PASSWORD_EXPIRE_IN_DAYS

from invenio.legacy.dbquery import run_sql


def create_doi(recid=None):
    """ Generate a new DOI """
    if recid is None:
        recid = run_sql("INSERT INTO bibrec (creation_date, modification_date)"
                        " VALUES (NOW(), NOW())")

    return dict(
        doi='%s/zenodo.%s' % (
            current_app.config['CFG_DATACITE_DOI_PREFIX'],
            recid
        ),
        recid=recid,
    )


def filter_empty_helper(keys=None):
    """ Remove empty elements from a list"""
    def _inner(elem):
        if isinstance(elem, dict):
            for k, v in elem.items():
                if (keys is None or k in keys) and v:
                    return True
            return False
        else:
            return bool(elem)
    return _inner


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


def get_file_links(recid):
    from invenio.modules.formatter.format_elements.bfe_fulltext import _CFG_BIBFORMAT_HIDDEN_DOCTYPES, get_files
    from invenio.modules.formatter.engine import BibFormatObject

    bfo = BibFormatObject(recid)

    (parsed_urls, old_versions, additionals) = get_files(bfo, distinguish_main_and_additional_files=True,
                                                         include_subformat_icons=True,
                                                         hide_doctypes=_CFG_BIBFORMAT_HIDDEN_DOCTYPES)

    main_urls = parsed_urls['main_urls']
    fulltexts = main_urls['Fulltext'] if 'Fulltext' in main_urls else []

    files = []
    for f in fulltexts:
        if len(f[1]) > 37 and f[1].count('-') >= 5:
            files.append([f[0], '.'.join([f[1][37:], f[2]])])
        else:
            files.append([f[0], '.'.join([f[1], f[2]])])

    return files


def create_authors_ttf(bfo):
    authors = []
    for entry in bfo.fields('100'):
        affiliation = " (%(aff)s%(city)s%(country)s)" % {'aff': entry['n'] if 'n' in entry else '',
                                                         'city': ", " + entry['k'] if 'k' in entry else '',
                                                         'country': " (" + entry['l'] + ')' if 'l' in entry else '',
                                                         }

        author = """%(familyname)s, %(firstname)s%(affiliation)s%(email)s"""

        author = author % {'firstname': entry['b'],
                           'familyname': entry['a'],
                           'affiliation': affiliation if 'n' in entry else '',
                           'email': ', ' + entry['e'] if 'e' in entry else '',
                           }

        authors.append(author)

    return '; '.join(authors)


def create_control_data(bfo):

    d = {}
    for field in bfo.fields('908'):
        d.update(field)

    import collections
    d = collections.defaultdict(list)
    for field in bfo.fields('908'):
        for k, v in field.iteritems():
            d[k].append(v)

    abstracts_no = len(bfo.fields('860'))

    indicators = ''
    descriptors = bfo.fields('800__a')

    if abstracts_no == 0:
        indicators += 'E'

    if len(bfo.fields('210')) > 0:
        indicators += 'K'

    for descriptor in ["COMPILED DATA", "EVALUATED DATA", "EXPERIMENTAL DATA",
                       "NUMERICAL DATA", "STATISTICAL DATA", "THEORETICAL DATA"]:
        if descriptor in descriptors:
            indicators += 'N'

    if "LEGISLATIVE TEXT" in descriptors:
        indicators += 'Q'

    if len(bfo.fields('610')) > 0:
        indicators += 'T'

    if len(bfo.fields('110')) > 0:
        indicators += 'U'

    if "COMPUTER PROGRAM DOCUMENTATION" in descriptors:
        indicators += 'V'

    if "STANDARDS DOCUMENT" in descriptors:
        indicators += 'W'

    if len(bfo.fields('611')) > 0:
        indicators += 'X'

    if "PROGRESS REPORT" in descriptors:
        indicators += 'Y'

    if "BIBLIOGRAPHIES" in descriptors:
        indicators += 'Z'

    indicators = ''.join(sorted(set(indicators)))

    subjects = ''
    record_type = ''
    if 'a' in d:
        subjects = ';'.join(d['a'])
    if 'c' in d:
        record_type = d['c'][0]

    levels = 'M'

    elements = [subjects, "%02d" % abstracts_no, record_type, levels, indicators]
    elements = [e for e in elements if e]

    return '/'.join(elements)


def create_languages_ttf(res):
    out = '('
    for tag in res:
        out += tag[1] + ', '
    return out.strip(' ,') + ')'


def create_place_ttf(d):
    places = []
    for entry in d:
        places.append("%(city)s (%(country)s)" % {'city': entry['a'] if 'a' in entry else '',
                                                  'country': entry['b'] if 'b' in entry else ''})
    return ', '.join(places)


def create_date_ttf(d):

    d1 = str(d['a']).strip() if 'a' in d else ''
    d2 = str(d['e']).strip() if 'e' in d else ''

    s1 = CFG_SEASON_CODES[int(d['c'])][0] if 'c' in d else ''
    s2 = CFG_SEASON_CODES[int(d['g'])][0] if 'g' in d else ''

    m1 = CFG_MONTH_CODES[int(d['b'])][0] if 'b' in d else s1
    m2 = CFG_MONTH_CODES[int(d['f'])][0] if 'f' in d else s2

    y1 = str(d['d']).strip() if 'd' in d else ''
    y2 = str(d['h']).strip() if 'h' in d else ''

    if y1 == y2:
        if m1 == m2:  # -> "dd-dd mmm yyyy"
            z = "%(from)s%(separator)s%(to)s %(m)s %(y)s" % \
                {'y': y1,
                 'm': m1,
                 'from': d1,
                 'to': d2,
                 'separator': '-' if d1 and d2 else ''}

        else:  # m1 != m2  -> "dd mmm - dd mmm yyyy"
            month_from = "%(day)s%(separator)s%(month)s" % {'day': d1,
                                                            'separator': ' ' if d1 else '',
                                                            'month': m1}
            month_to = "%(day)s%(separator)s%(month)s" % {'day': d2,
                                                          'separator': ' ' if d2 else '',
                                                          'month': m2}
            z = "%(from)s%(separator)s%(to)s %(y)s" % \
                {'y': y1,
                 'm': m1,
                 'from': month_from,
                 'to': month_to,
                 'separator': ' - ' if d2 else ('-' if month_to else '')}

    else:  # y1 != y2 -> "dd mmm yyyy - dd mmm yyyy"
        date_from = "%(day)s%(separator_d)s%(month)s%(separator_m)s%(year)s" % \
                    {'day': d1 if m1 else '',
                     'month': m1,
                     'year': y1,
                     'separator_d': ' ' if d1 else '',
                     'separator_m': ' ' if m1 else ''}

        date_to = "%(day)s%(separator_d)s%(month)s%(separator_m)s%(year)s" % \
                  {'day': d2 if m2 else '',
                   'month': m2,
                   'year': y2,
                   'separator_d': ' ' if d2 else '',
                   'separator_m': ' ' if m2 else ''}
        z = "%(from)s%(separator)s%(to)s" % {'from': date_from,
                                             'to': date_to,
                                             'separator': ' - ' if m2 else ('-' if date_to else '')}

    return z.strip(' ,')


def must_switch(d1, d2):
    if 'year' not in d2:
        return False
    if d1['year'] != d2['year']:
        return int(d1['year']) > int(d2['year'])

    if 'month' in d1 and 'month' in d2:
        if d1['month'] != d2['month']:
            return int(d1['month']) > int(d2['month'])
        if 'day' in d1 and 'day' in d2:
            return d1['day'] > d2['day']
    elif 'season' in d1 and 'season' in d2:
        return int(d1['season']) > int(d2['season'])

    return False


def update_progress(progress):
    sys.stdout.write('\r[{0}{1}] {2}% '.format('#'*(int(progress)),
                     ' '*(100-int(progress)),
                     round(progress, 2)))
    sys.stdout.flush()


def load_knowledge_bases():
    from inis.demosite.lang_codes import CFG_LANG_CODES
    load_kb('languages', CFG_LANG_CODES)

    from inis.demosite.descriptors_en import descriptors_en
    load_kb('descriptors', descriptors_en)
    from inis.demosite.subjects import subjects
    load_kb('subjects', subjects)

    from inis.demosite.members import CFG_COUNTRIES_DICT, CFG_MEMBERS_DICT, CFG_ORGANIZATIONS_DICT

    load_kb('countries', CFG_COUNTRIES_DICT)
    load_kb('organizations', CFG_ORGANIZATIONS_DICT)
    load_kb('members', CFG_MEMBERS_DICT)


def load_kb(name, terms):
    import invenio.modules.knowledge.api as kb

    print(">>> Loading %s..." % name)

    if kb.kb_exists(name):
        kb.delete_kb(name)
    kb.add_kb(name)
    knowledge_base = kb.get_kb_by_name(name)

    is_dictionary = isinstance(terms, dict)
    t = float(len(terms))
    i = 1

    for d in terms:
        value = terms[d] if is_dictionary else d
        knowledge_base.kbrvals.set(kb.models.KnwKBRVAL(m_key=d, m_value=value))
        update_progress(i*100/t)
        i += 1

    print(" Done!!!")


def get_kb_items(name, as_dictionary=False):
    from invenio.modules.knowledge.api import get_kbr_items

    try:
        items = get_kbr_items(name)
    except:
        return []
    items = [(i['key'], i['value']) for i in items]

    if as_dictionary:
        items = dict(items)

    return items


def get_kb_value(name, key):
    from invenio.modules.knowledge.api import get_kb_mapping
    mapping = get_kb_mapping(kb_name=name, key=key)
    return mapping['value'] if mapping else None


def get_kb_key(name, value):
    from invenio.modules.knowledge.api import get_kb_mapping
    mapping = get_kb_mapping(kb_name=name, value=value)
    return mapping['key'] if mapping else None
