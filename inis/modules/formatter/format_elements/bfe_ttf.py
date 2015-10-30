# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHformatted_tags ANY WARRANTY; withformatted_tags even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
"""BibFormat element - Prints TTF
"""

from inis.utils import create_authors_ttf, create_control_data, create_date_ttf, create_place_ttf


def format_element(bfo, mode='text'):

    skip_tags = set(['100', '213', '401', '403', '856', '600', '908', '980', '911', '913', '999'])
    tags = [tag for tag in bfo.get_record().keys() if not tag.startswith('00') and tag not in skip_tags]

    formatted_tags = []
    formatted_tags.append(['001', bfo.field('911__a')])
    formatted_tags.append(['008', create_control_data(bfo)])
    formatted_tags.append(['100', create_authors_ttf(bfo)])
    formatted_tags.append(['600', '(' + ', '.join(bfo.fields('600__a')) + ')'])
    formatted_tags.append(['401', create_place_ttf(bfo.fields('401'))])
    formatted_tags.append(['403', create_date_ttf(bfo.field('403'))])
    formatted_tags.append(['213', create_date_ttf(bfo.field('213'))])

    for tag in tags:
        formatted_tags.append([tag, '; '.join(bfo.fields(tag + '__a'))])
    formatted_tags = [tag for tag in formatted_tags if tag[1]]

    formatted_tags.sort()

    out = ""
    prefix = "%s^"
    postfix = "\n"

    if mode == 'xml':
        out += '<inisrecord>\n'
        prefix = "<tag name='%s'>"
        postfix = "</tag>\n"

    for [tag, value] in formatted_tags:
        out += prefix % tag
        out += value
        out += postfix

    if mode == 'xml':
        out += '</inisrecord>\n'

    return out


def escape_values(bfo):
    """
    Called by BibFormat in order to check if formatted_tagsput of this element
    should be escaped.
    """
    return 0
