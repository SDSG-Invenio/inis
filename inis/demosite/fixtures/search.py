# -*- coding: utf-8 -*-
#
# This file is part of Zenodo.
# Copyright (C) 2014 CERN.
#
# Zenodo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Zenodo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Zenodo. If not, see <http://www.gnu.org/licenses/>.
#
# In applying this licence, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

from fixture import DataSet

from inis.config import CFG_MEMBERS_NAMES

from invenio.modules.search import fixtures


# ===========
# Collections
# ===========
class CollectionData(DataSet):
    pass

colls = []
colls.append((2, 'Rejected', 'Rejected', '980__a:Rejected'))

i = 3
for name in CFG_MEMBERS_NAMES:
    colls.append((i, name, name, '980__a:'+name, ))
    i = i + 1
    colls.append((i, name, 'r-'+name, '980__b:'+name, ))
    i = i + 1

idx = 2
for i, t, n, q in colls:
    class obj(object):
        id = idx
        name = n
        dbquery = q
        names = {
            ('en', 'ln'): t,
        }
    obj.__name__ = n
    idx += 1
    setattr(CollectionData, n, obj)


class CollectiondetailedrecordpagetabsData(DataSet):
    pass

coll_ids = [1] + [x[0] for x in colls]

for cid in coll_ids:
    class obj(object):
        id_collection = cid
        tabs = 'usage;comments;metadata;files'
    obj.__name__ = "ctabs%s" % cid
    setattr(CollectiondetailedrecordpagetabsData, obj.__name__, obj)


# ===============
# Collection Tree
# ===============
order = 1
coll_coll_data = []
for i, t, n, q in colls[1:]:  # we exclude 'Rejected' from the tree
    if n.startswith('r-'):
        father = 2
    else:
        father = 1
    coll_coll_data.append((father, i, 'r', order))
    order = order + 1
coll_coll_data = tuple(coll_coll_data)


class CollectionCollectionData(DataSet):
    pass


idx = 1
for d, s, t, scr in coll_coll_data:
    class obj(object):
        id_dad = d
        id_son = s
        score = scr
        type = t
    obj.__name__ = "cc%s" % idx
    idx += 1
    setattr(CollectionCollectionData, obj.__name__, obj)


# ===============
# Collection tabs
# ===============
class CollectiondetailedrecordpagetabsData(DataSet):
    pass

coll_ids = [1] + [x[0] for x in colls]

for cid in coll_ids:
    class obj(object):
        id_collection = cid
        tabs = 'usage;comments;metadata;files'
    obj.__name__ = "ctabs%s" % cid
    setattr(CollectiondetailedrecordpagetabsData, obj.__name__, obj)


class Field_45:
    code = u'trns'
    id = 45
    name = u'trns'
fixtures.FieldData.Field_45 = Field_45


class Tag_227:
    id = 227
    value = u'911__a'
    recjson_value = u'trns'
    name = u'trns'
fixtures.TagData.Tag_227 = Tag_227


class FieldTag_227_45:
    score = 100
    id_tag = fixtures.TagData.Tag_227.id
    id_field = fixtures.FieldData.Field_45.id
fixtures.FieldTagData.FieldTag_227_45 = FieldTag_227_45


class Field_46:
    code = u'member'
    id = 46
    name = u'member'
fixtures.FieldData.Field_46 = Field_46


class Tag_228:
    id = 228
    value = u'913__a'
    recjson_value = u'member'
    name = u'member'
fixtures.TagData.Tag_228 = Tag_228


class FieldTag_228_46:
    score = 100
    id_tag = fixtures.TagData.Tag_228.id
    id_field = fixtures.FieldData.Field_46.id
fixtures.FieldTagData.FieldTag_228_46 = FieldTag_228_46
