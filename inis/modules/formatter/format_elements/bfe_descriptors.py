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
"""BibFormat element - Prints descriptors
"""
__revision__ = "$Id$"


def format_element(bfo, separator=" ", highlight='no'):
    """
    Prints the titles of a record.

    @param separator: separator between the different titles
    @param highlight: highlights the words corresponding to search query if set to 'yes'
    """

    descriptors = bfo.fields('800__a')

    if not descriptors:
        return ''

    out = ''
    for d in descriptors:
        out += """<span class="label label-default"
                  data-toggle="tooltip"
                  title="proposed descriptor"
                  style="display:inline-block; margin-right: 5px;">
                  %s
                  </span>""" % (d, )

    return out


def escape_values(bfo):
    """
    Called by BibFormat in order to check if output of this element
    should be escaped.
    """
    return 0
