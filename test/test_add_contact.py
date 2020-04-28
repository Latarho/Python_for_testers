from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(first_name="", middle_name="", last_name="", title="", company="", address="", mobile="", work="", email="", notes="")] + [
    Contact(first_name=random_string("first_name", 10), middle_name=random_string("middle_name", 10),
    last_name=random_string("last_name", 10), title=random_string("title", 5),
    company=random_string("company", 5), address=random_string("address", 10), mobile=random_string("mobile", 10),
    work=random_string("work", 10), email=random_string("email", 10), notes=random_string("notes", 10))
    for i in range(5)]

@pytest.mark.parametrize("contact", testdata, ids = [repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)