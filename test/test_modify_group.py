from model.group import Group
from random import randrange

def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    old_groups = app.group.get_group_list()
    # Определение случайного индекса группы
    # Функция randrange генерирует значение от 0 до указанного (в данном случае len(old_groups)
    index = randrange(len(old_groups))
    group = Group(name="Modify_group_1")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_first_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test", header="test", footer="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="Modify_header_group_1"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
