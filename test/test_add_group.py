from model.group import Group

def test_add_group(app):
    app.group.create_group(Group(name="New_group_1", header="Header_new_group_1", footer="Footer_new_group_1"))

def test_add_empty_group(app):
    app.group.create_group(Group(name="", header="", footer=""))