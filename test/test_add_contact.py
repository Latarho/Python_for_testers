from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(first_name="Chebi", middle_name="Chebikovich", last_name="Cheb",
                                            title="Lil", company="Chebi GANG", address="Surikova street",
                                            mobile="8-800-555-555-555", email="orange@orange.com", notes="Little Gangster"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(first_name="", middle_name="", last_name="",
                                            title="", company="", address="",
                                            mobile="", email="", notes=""))
    app.session.logout()