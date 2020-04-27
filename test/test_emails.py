from random import randrange

def test_emails_on_home_page(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(contact_from_edit_page)

def test_emails_on_contact_view_page(app):
    index = randrange(app.contact.count())
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    assert contact_from_view_page.all_emails_from_view_page == app.contact.merge_emails_like_on_home_page(contact_from_edit_page)