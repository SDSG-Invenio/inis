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


def create_authors_ttf(d):
    out = ''
    for tag in d:
        affiliation = " (%(aff)s%(city)s%(country)s)" % {'aff': d[tag]['n'] if 'n' in d[tag] else '',
                                                         'city': ", " + d[tag]['k'] if 'k' in d[tag] else '',
                                                         'country': " (" + d[tag]['l'] + ')' if 'l' in d[tag] else '',
                                                         }

        author = """%(familyname)s, %(firstname)s%(affiliation)s%(email)s; """

        out += author % {'firstname': d[tag]['b'],
                         'familyname': d[tag]['a'],
                         'affiliation': affiliation if 'n' in d[tag] else '',
                         'email': ', ' + d[tag]['e'] if 'e' in d[tag] else '',
                         }
    return out.strip(' ;')


def create_languages_ttf(res):
    out = '('
    for tag in res:
        out += tag[1] + ', '
    return out.strip(' ,') + ')'


def create_place_ttf(d):
    out = ''
    for tag in d:
        out += "%(city)s (%(country)s), " % {'city': d[tag]['a'] if 'a' in d[tag] else '',
                                             'country': d[tag]['b'] if 'b' in d[tag] else ''}
    return out.strip(' ,')


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


def record_get_ttf(recID, mode='text', on_the_fly=False):
    """
    Returns an XML string of the record given by recID.

    The function builds the XML directly from the database,
    without using the standard formatting process.

    'format' allows to define the flavour of XML:
        - 'xm' for standard XML
        - 'marcxml' for MARC XML
        - 'oai_dc' for OAI Dublin Core
        - 'xd' for XML Dublin copy_reg

    If record does not exist, returns empty string.
    If the record is deleted, returns an empty MARCXML (with recid
    controlfield, OAI ID fields and 980__c=DELETED)

    @param recID: the id of the record to retrieve
    @param format: the format to use
    @param on_the_fly: if False, try to fetch precreated one in database
    @param decompress: the library to use to decompress cache from DB
    @return: the xml string of the record
    """
    from invenio.legacy.search_engine import record_exists
    from xml.sax.saxutils import escape as encode_for_xml

    def get_creation_date(recID, fmt="%Y-%m-%d"):
        "Returns the creation date of the record 'recID'."
        out = ""
        res = run_sql("SELECT DATE_FORMAT(creation_date,%s) FROM bibrec WHERE id=%s", (fmt, recID), 1)
        if res:
            out = res[0][0]
        return out

    def get_modification_date(recID, fmt="%Y-%m-%d"):
        "Returns the date of last modification for the record 'recID'."
        out = ""
        res = run_sql("SELECT DATE_FORMAT(modification_date,%s) FROM bibrec WHERE id=%s", (fmt, recID), 1)
        if res:
            out = res[0][0]
        return out

    skip_tags = set(['100', '213', '401', '403', '856', '600', '980', '911'])

    out = ""
    prefix = "%s^"
    postfix = "\n"

    if mode == 'xml':
        out += '<inisrecord>\n'
        prefix = "<tag name='%s'>"
        postfix = "</tag>"

    # sanity check:
    record_exist_p = record_exists(recID)
    if record_exist_p == 0:  # doesn't exist
        return out

    # record 'recID' is not formatted in 'format' -- they are
    # not in "bibfmt" table; so fetch all the data from
    # "bibXXx" tables:
    # out += "001^%d\n" % int(recID)
    if record_exist_p == -1:
        # deleted record, so display only 980:
        out += "<datafield tag=\"980\" ind1=\" \" ind2=\" \"><subfield code=\"c\">DELETED</subfield></datafield>\n"
        from invenio.legacy.search_engine import get_merged_recid
        merged_recid = get_merged_recid(recID)
        if merged_recid:  # record was deleted but merged to other record, so display this information:
            out += "<datafield tag=\"970\" ind1=\" \" ind2=\" \"><subfield code=\"d\">%d</subfield></datafield>\n" % merged_recid
    else:
        # controlfields
        query = "SELECT b.tag,b.value,bb.field_number FROM bib91x AS b, bibrec_bib91x AS bb "\
                "WHERE bb.id_bibrec='%s' AND b.id=bb.id_bibxxx AND b.tag like '911%%' "\
                "ORDER BY bb.field_number, b.tag ASC" % recID
        res = run_sql(query)
        for row in res:
            field, value = row[0], row[1]
            value = encode_for_xml(value)
            if mode == 'xml':
                out += """<tag name='001'>%s</tag>""" % (encode_for_xml(value), )
            else:
                out += """001^%s\n""" % (value, )

        query = "SELECT b.tag,b.value,bb.field_number FROM bib00x AS b, bibrec_bib00x AS bb "\
                "WHERE bb.id_bibrec='%s' AND b.id=bb.id_bibxxx AND b.tag like '009%%' "\
                "ORDER BY bb.field_number, b.tag ASC" % recID
        res = run_sql(query)
        for row in res:
            field, value = row[0], row[1]
            value = encode_for_xml(value)
            if mode == 'xml':
                out += """<tag name='009'>%s</tag>""" % (encode_for_xml(value), )
            else:
                out += """009^%s\n""" % (encode_for_xml(value), )

        # datafields
        i = 1
        # Do not process bib00x and bibrec_bib00x, as
        # they are controlfields. So start at bib01x and
        # bibrec_bib00x (and set i = 0 at the end of
        # first loop)

        # authors
        query = "SELECT b.tag,b.value,bb.field_number FROM bib10x AS b, bibrec_bib10x AS bb "\
                "WHERE bb.id_bibrec='%s' AND b.id=bb.id_bibxxx AND b.tag like '100%%' "\
                "ORDER BY bb.field_number, b.tag ASC" % recID
        res = run_sql(query)

        d = {}
        for row in res:
            field, value, tag = row[0][-1], row[1], row[2]
            if tag not in d:
                d[tag] = {}
            d[tag][field] = value

        value = create_authors_ttf(d)

        out += prefix % ('100', ) + encode_for_xml(value) + postfix if value != '' else ''

        # languages
        query = "SELECT b.tag,b.value,bb.field_number FROM bib60x AS b, bibrec_bib60x AS bb "\
                "WHERE bb.id_bibrec='%s' AND b.id=bb.id_bibxxx AND b.tag like '600%%' "\
                "ORDER BY bb.field_number, b.tag ASC" % recID
        res = run_sql(query)

        out += prefix % ('600', )
        value = create_languages_ttf(res)
        out += "%s" % (encode_for_xml(value), )
        out += postfix

        # place
        query = "SELECT b.tag,b.value,bb.field_number FROM bib40x AS b, bibrec_bib40x AS bb "\
                "WHERE bb.id_bibrec='%s' AND b.id=bb.id_bibxxx AND b.tag like '401%%' "\
                "ORDER BY bb.field_number, b.tag ASC" % recID
        res = run_sql(query)

        d = {}
        for row in res:
            field, value, tag = row[0][-1], row[1], row[2]
            if tag not in d:
                d[tag] = {}
            d[tag][field] = value

        out += prefix % ('401', )
        value = create_place_ttf(d)
        out += "%s" % (encode_for_xml(value), )
        out += postfix

        # dates
        query = "SELECT b.tag,b.value,bb.field_number FROM bib40x AS b, bibrec_bib40x AS bb "\
                "WHERE bb.id_bibrec='%s' AND b.id=bb.id_bibxxx AND b.tag like '403%%' "\
                "ORDER BY bb.field_number, b.tag ASC" % recID
        res = run_sql(query)

        d = {}
        for row in res:
            field, value = row[0][-1], row[1]
            d[field] = value

        out += prefix % ('403', )
        value = create_date_ttf(d)
        out += "%s" % (encode_for_xml(value), )
        out += postfix

        query = "SELECT b.tag,b.value,bb.field_number FROM bib21x AS b, bibrec_bib21x AS bb "\
                "WHERE bb.id_bibrec='%s' AND b.id=bb.id_bibxxx AND b.tag like '213%%' "\
                "ORDER BY bb.field_number, b.tag ASC" % recID
        res = run_sql(query)

        d = {}
        for row in res:
            field, value = row[0][-1], row[1]
            d[field] = value

        out += prefix % ('213', )
        value = create_date_ttf(d)
        out += "%s" % (encode_for_xml(value), )
        out += postfix

        # other tags
        for digit1 in range(0, 10):
            for digit2 in range(i, 10):
                bx = "bib%d%dx" % (digit1, digit2)
                bibx = "bibrec_bib%d%dx" % (digit1, digit2)
                query = "SELECT b.tag,b.value,bb.field_number FROM %s AS b, %s AS bb "\
                        "WHERE bb.id_bibrec='%s' AND b.id=bb.id_bibxxx AND b.tag LIKE '%s%%' "\
                        "ORDER BY bb.field_number, b.tag ASC" % (bx,
                                                                 bibx,
                                                                 recID,
                                                                 str(digit1)+str(digit2))
                res = run_sql(query)
                field_old = ""
                for row in res:
                    field, value = row[0], row[1]
                    if field[:3] not in skip_tags:
                        # print field tag
                        if field != field_old:
                            out += prefix % (field[:3], )
                        else:
                            out += ";"

                        field_old = field
                        # print subfield value
                        out += "%s" % (encode_for_xml(value), )
                        out += postfix

                # all fields/subfields printed in this run, so close the tag:
                # if field_old != -999:
                #     out += """\n"""
            i = 0  # Next loop should start looking at bib%0 and bibrec_bib00x
    # we are at the end of printing the record
    if mode == 'xml':
        out += '</inisrecord>\n'

    return out.strip()


# def process_date(d):
#     if 'publication_date' in d:
#         if 'date_from' in d['publication_date']:
#             d['publication_date_from'] = d['publication_date']['date_from']
#             if 'month' in d['publication_date_from'] and int(d['publication_date_from']['month']) > 20:
#                 d['publication_date_from']['season'] = int(d['publication_date_from']['month']) - 20
#                 d['publication_date_from'].pop('month')
#                 d['publication_date_from'].pop('day')
#         if 'date_to' in d['publication_date']:
#             d['publication_date_to'] = d['publication_date']['date_to']
#             if 'month' in d['publication_date_to'] and int(d['publication_date_to']['month']) > 20:
#                 d['publication_date_to']['season'] = int(d['publication_date_to']['month']) - 20
#                 d['publication_date_to'].pop('month')
#                 d['publication_date_to'].pop('day')
#     return d


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
