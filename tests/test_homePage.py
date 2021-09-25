import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testdata.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, get_data):
        # driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        # driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
        # driver.get("https://rahulshettyacademy.com/angularpractice/") # this will come from conftest.py

        # driver.find_element_by_name("name").send_keys("Rahul")

        homepage = HomePage(self.driver)
        # homepage.send_name().send_keys(get_data[0])
        log = self.getLogger()
        log.info("First name is " + get_data["firstname"])
        homepage.send_name().send_keys(get_data["firstname"])
        # homepage.send_email().send_keys(get_data[1])
        homepage.send_email().send_keys(get_data["lastname"])

        homepage.set_example_check().click()

        # select class provide the methods to handle the options in dropdown
        # dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
        # dropdown.select_by_visible_text("Female")
        # dropdown.select_by_index(0)

        # dropdown = Select(homepage.select_dropdown())
        # dropdown.select_by_visible_text("Female")
        # dropdown.select_by_index(0)
        # self.select_gender(homepage.option_select_dropdown(), get_data[2])
        self.select_gender(homepage.option_select_dropdown(), get_data["gender"])

        homepage.select_submit().click()

        message = homepage.get_success_message().text

        assert "success" in message
        self.driver.refresh()

    # @pytest.fixture(params=[("Shubham", "Kalambe", "Male"), ("XYZ", "YZX", "Female")])
    # def get_data(self, request):
    #     return request.param

    # @pytest.fixture(params=[{"firstname": "shu", "lastname": "kal", "gender": "Male"}, {"firstname": "bhu", "lastname": "kal", "gender": "Female"}])
    # def get_data(self, request):
    #     return request.param

    @pytest.fixture(params=HomePageData.get_test_data("Testcase2"))
    def get_data(self, request):
        return request.param
