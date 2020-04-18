from selenium import webdriver
from contact import Contact
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path ="C:/Users/latar/chromedriver/chromedriver.exe")
        self.driver.implicitly_wait(30)

    def test_add_contact(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username="admin", password="secret")
        self.create_contact(driver, Contact(first_name="Chebi", middle_name="Chebikovich", last_name="Cheb",
                                            title="Lil", company="Chebi GANG", address="Surikova street",
                                            mobile="8-800-555-555-555", email="orange@orange.com", notes="Little Gangster"))
        self.return_to_contact_page(driver)
        self.logout(driver)

    def test_add_empty_contact(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username="admin", password="secret")
        self.create_contact(driver, Contact(first_name="", middle_name="", last_name="",
                                            title="", company="", address="",
                                            mobile="", email="", notes=""))
        self.return_to_contact_page(driver)
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def create_contact(self, driver, contact):
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

    def login(self, driver, username, password):
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/group.php")

    def return_to_contact_page(self, driver):
        driver.find_element_by_xpath("//*[@id='content']/div/i/a[2]").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()