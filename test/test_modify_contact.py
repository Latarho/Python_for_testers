from model.contact import Contact

def test_modify_first_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(first_name="Gena"))
    app.session.logout()

#def test_modify_first_contact_middlename(app):
    #app.session.login(username="admin", password="secret")
    #app.contact.modify_first_contact(Contact(middle_name="Genakovich"))
    #app.session.logout()

# def test_modify_first_contact(app):
   # app.session.login(username="admin", password="secret")
   # app.contact.modify_first_contact(Contact(first_name="Chebi", middle_name="Chebikovich", last_name="Genarek",
   #                                         title="Lil", company="Chebi GANG", address="Surikova street",
   #                                         mobile="8-800-555-555-555", email="orange@orange.com", notes="Little Gangster"))
   # app.session.logout()