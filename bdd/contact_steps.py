from pytest_bdd import given, when, then
from model.contact import Contact
import random

@given('a contact list')
def contact_list(db):
    return db.get_contact_list()

@given('a contact with <first_name>, <last_name> and <mobile>')
def new_contact(first_name, last_name, mobilephone):
    return Contact(first_name=first_name, last_name=last_name, mobile=mobilephone)

@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)

@then('The new contact list is equal to the old list with the added contact')
def verify_group_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.group.create(Contact(first_name='Some firstname', last_name='Some lastname'))
    return db.get_contact_list()

@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('I delete a contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_index(random_contact.id)

@then('the new list is equal to the old list without the deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.group.get_contact_list(), key=Contact.id_or_max)

@when('I modify a contact from the list')
def modify_contact(app, random_contact):
    new_contact = Contact(first_name="Vova", last_name="Putin")
    app.contact.modify_contact_by_index(random_contact.id, new_contact)

@then('the new list is equal to the old list with modified contact')
def verify_contact_modified(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    new_contact = Contact(first_name="Vova", last_name="Putin")
    for i in old_contacts:
        if i.id == random_contact.id:
            i.firstname = new_contact.first_name
            i.lastname = new_contact.last_name
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)