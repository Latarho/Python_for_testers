from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()

    contact = Contact(first_name="Chebi", middle_name="Chebikovich", last_name="Cheb",
                                            title="Lil", company="Chebi GANG", address="Surikova street",
                                            mobile="8800555555555", work="1234567890", email="orange@orange.com", notes="Little Gangster")

    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()

    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)