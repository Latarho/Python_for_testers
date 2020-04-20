from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        driver = self.app.driver
        # init contact creators
        driver.find_element_by_xpath("//*[@id='nav']/ul/li[2]/a").click()
        self.fill_contact_form(contact)
        # submit contact creation
        driver.find_element_by_name("submit").click()
        self.return_to_contact_page()

    def fill_contact_form(self, contact):
        driver = self.app.driver
        self.change_filed_contact("firstname", contact.first_name)
        self.change_filed_contact("middlename", contact.middle_name)
        self.change_filed_contact("lastname", contact.last_name)
        self.change_filed_contact("title", contact.title)
        self.change_filed_contact("company", contact.company)
        self.change_filed_contact("address", contact.address)
        self.change_filed_contact("mobile", contact.mobile)
        self.change_filed_contact("email", contact.email)
        self.change_filed_contact("notes", contact.notes)

    def change_filed_contact(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        driver = self.app.driver
        self.select_first_contact()
        # submit deletion
        driver.find_element_by_css_selector("input[value='Delete']").click()
        #driver.find_element_by_xpath("//*[@id='content']/form[2]/div[2]/input").click()
        driver.switch_to_alert().accept()

    def select_first_contact(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        driver = self.app.driver
        self.select_first_contact()
        # init contact modify
        driver.find_element_by_xpath("//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modify
        driver.find_element_by_xpath("//*[@id='content']/form[1]/input[22]").click()
        # return to contact page from update
        driver.find_element_by_xpath("//*[@id='content']/div/i/a").click()

    def return_to_contact_page(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//*[@id='content']/div/i/a[2]").click()

    def count(self):
        driver = self.app.driver
        return len(driver.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        driver = self.app.driver
        contacts = []
        for element in driver.find_elements_by_css_selector("tr.odd"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(first_name=text, id=id))
        return contacts