from model.contact import Contact
from random import randrange

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test", middle_name="test", last_name="test",
                                   title="test", company="test", address="test",
                                   mobile="test", work="test", email="test", notes="test"))
    old_contacts = app.contact.get_contact_list()

    index = randrange(2, len(old_contacts)+2)
    contact = Contact(first_name="Gena", last_name="Crocodile")
    contact.id = old_contacts[index-2].id
    app.contact.modify_contact_by_index(index, contact)

    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()

    old_contacts[index-2] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)