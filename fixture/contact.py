class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        driver = self.app.driver
        # init contact creators
        driver.find_element_by_xpath("//*[@id='nav']/ul/li[2]/a").click()
        # fill contact form
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.first_name)
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(contact.middle_name)
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.last_name)
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(contact.title)
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(contact.company)
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(contact.mobile)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_name("notes").click()
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys(contact.notes)
        # submit contact creation
        driver.find_element_by_name("submit").click()
        self.return_to_contact_page()

    def delete_first_contact(self):
        driver = self.app.driver
        # select first contact
        driver.find_element_by_name("selected[]").click()
        # submit deletion
        driver.find_element_by_xpath("//*[@id='content']/form[2]/div[2]/input").click()
        driver.switch_to_alert().accept()

    def return_to_contact_page(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//*[@id='content']/div/i/a[2]").click()