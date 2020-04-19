from model.group import Group

def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="Modify_group_1", header="Header_modify_group_1", footer="Footer_modify_group_1"))
    app.session.logout()