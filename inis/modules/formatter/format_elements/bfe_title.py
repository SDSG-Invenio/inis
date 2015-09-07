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
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
"""BibFormat element - Prints titles
"""

import cgi

__revision__ = "$Id$"


def format_element(bfo, separator=" ", highlight='no'):
    """
    Prints the titles of a record.

    @param separator: separator between the different titles
    @param highlight: highlights the words corresponding to search query if set to 'yes'
    """

    title = bfo.field('200__a')
    title = cgi.escape(title)

    title_original = bfo.field('230__a')
    title_original = cgi.escape(title_original)

    if highlight == 'yes':
        from invenio.modules.formatter import utils as bibformat_utils
        title = bibformat_utils.highlight(title, bfo.search_pattern)
        # title_original = bibformat_utils.highlight(title_original, bfo.search_pattern)

    out = title
    if title_original:
        out += "%s(<small>%s</small>)" % (separator, title_original)
    return out


def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0
