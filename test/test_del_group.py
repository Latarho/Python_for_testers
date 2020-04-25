from model.group import Group
from random import randrange

def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    old_groups = app.group.get_group_list()
    # Определение случайного индекса группы
    # Функция randrange генерирует значение от 0 до указанного (в данном случае len(old_groups)
    index = randrange(len(old_groups))
    # В качестве парметра передаем выбарнный индекс
    app.group.delete_group_by_index(index)

    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == app.group.count()

    old_groups[index:index+1] = []
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)