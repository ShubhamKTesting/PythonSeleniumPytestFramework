from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    example_check = (By.ID, "exampleCheck1")
    select_dropdown = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    success_message = (By.CLASS_NAME, "alert-success")

    def ShopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def send_name(self):
        return self.driver.find_element(*HomePage.name)

    def send_email(self):
        return self.driver.find_element(*HomePage.email)

    def set_example_check(self):
        return self.driver.find_element(*HomePage.example_check)

    def option_select_dropdown(self):
        return self.driver.find_element(*HomePage.select_dropdown)

    def select_submit(self):
        return self.driver.find_element(*HomePage.submit)

    def get_success_message(self):
        return self.driver.find_element(*HomePage.success_message)
