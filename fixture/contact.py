from model.contact import Contact
import re

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
        self.contact_cache = None
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
        self.change_filed_contact("work", contact.work)
        self.change_filed_contact("email", contact.email)
        self.change_filed_contact("notes", contact.notes)

    def change_filed_contact(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        driver = self.app.driver
        self.select_contact_by_index(index)
        driver.find_element_by_css_selector("input[value='Delete']").click()
        driver.switch_to_alert().accept()
        self.contact_cache = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        driver = self.app.driver
        # Среди всех элементов (контактов) выбираем по индексу нужный и клик
        driver.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        driver = self.app.driver
        self.select_first_contact()
        driver.find_element_by_xpath("//*[@id='maintable']/tbody/tr[2]/td[8]/a/img".format(index)).click()
        self.fill_contact_form(new_contact_data)
        driver.find_element_by_xpath("//*[@id='content']/form[1]/input[22]").click()
        driver.find_element_by_xpath("//*[@id='content']/div/i/a").click()
        self.contact_cache = None

    def return_to_contact_page(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//*[@id='content']/div/i/a[2]").click()

    def count(self):
        driver = self.app.driver
        self.app.open_home_page()
        return len(driver.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.app.open_home_page()
            self.contact_cache = []
            for row in driver.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                first_name = cells[1].text
                last_name = cells[2].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, id=id,
                                                  all_phones_from_home_page = all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        first_name = driver.find_element_by_name("firstname").get_attribute("value")
        last_name = driver.find_element_by_name("lastname").get_attribute("value")
        id = driver.find_element_by_name("id").get_attribute("value")
        mobilephone = driver.find_element_by_name("mobile").get_attribute("value")
        workphone = driver.find_element_by_name("work").get_attribute("value")
        return Contact(first_name = first_name, last_name = last_name, id = id, mobile = mobilephone, work=workphone)

    def get_contact_from_view_page(self, index):
        driver = self.app.driver
        self.open_contact_view_by_index(index)
        text = driver.find_element_by_id("content").text
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        return Contact(mobile=mobilephone, work=workphone)