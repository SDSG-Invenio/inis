from inis.utils import get_kb_value, id_generator, set_password


def create_user(name, email, country):
    from invenio.ext.sqlalchemy import db
    from invenio.modules.accounts.models import User, Usergroup, UserUsergroup

    u = User(email=email, nickname=name, password=id_generator())
    db.session.add(u)
    db.session.commit()

    ug = Usergroup.query.filter_by(name=get_kb_value('members', country)).first()
    ug.users.append(UserUsergroup(id_user=u.id))
    db.session.add(ug)
    db.session.commit()

    set_password(email)


def get_deposition(order=0, sip=True):
    from invenio.modules.deposit.models import Deposition
    depositions = Deposition.get_depositions()
    d = depositions[order]
    if sip:
        return d.get_latest_sip()
    else:
        return d
