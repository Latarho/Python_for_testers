from model.group import Group

def test_add_group(app):
    old_groups = app.group.get_group_list()

    group = Group(name="New_group_1", header="Header_new_group_1", footer="Footer_new_group_1")

    app.group.create_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == app.group.count()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)