from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test", middle_name="test", last_name="test",
                                   title="test", company="test", address="test",
                                   mobile="test", email="test", notes="test"))
    app.contact.delete_first_contact()