from model.contact import Contact

def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test", middle_name="test", last_name="test",
                                   title="test", company="test", address="test",
                                   mobile="test", email="test", notes="test"))
    app.contact.modify_first_contact(Contact(first_name="Gena"))

#def test_modify_first_contact_middlename(app):
    #app.contact.modify_first_contact(Contact(middle_name="Genakovich"))

# def test_modify_first_contact(app):
   # app.contact.modify_first_contact(Contact(first_name="Chebi", middle_name="Chebikovich", last_name="Genarek",
   #                                         title="Lil", company="Chebi GANG", address="Surikova street",
   #                                         mobile="8-800-555-555-555", email="orange@orange.com", notes="Little Gangster"))