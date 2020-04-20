from model.group import Group

def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    app.group.modify_first_group(Group(name="Modify_group_1"))

def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    app.group.modify_first_group(Group(header="Modify_header_group_1"))

def test_modify_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    app.group.modify_first_group(Group(footer="Modify_footer_group_1"))