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
"""BibFormat element - Prints publisher
"""

from inis.utils import get_kb_value

__revision__ = "$Id$"


def format_element(bfo):
    """
    Prints the titles of a record.

    @param separator: separator between the different titles
    @param highlight: highlights the words corresponding to search query if set to 'yes'
    """

    place = bfo.field('401')
    publisher = bfo.field('402__a')
    city = place['a']
    country_code = place['b']
    country = get_kb_value('countries', country_code)

    template = "%(publisher)s%(city)s%(country)s"

    return template % {'publisher': publisher,
                       'city': " - %s" % city if city else '',
                       'country': " (%s)" % country if country else ''}


def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0
