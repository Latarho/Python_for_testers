from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/latar/chromedriver/chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/group.php")

    def destroy(self):
        self.driver.quit()