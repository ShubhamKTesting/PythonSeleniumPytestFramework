from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pytest

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()

        # 1st way

        # list_of_mob = driver.find_elements_by_xpath("//button[@class='btn btn-info']/../../div/h4/a")
        #
        # for mob in list_of_mob:
        #     if mob.text == "Blackberry":
        #         mob.find_element_by_xpath("//a[text()='Blackberry']/parent::h4/parent::div/parent::div/div[@class='card-footer']/button").click()

        # 2nd way
        home_page = HomePage(self.driver)
        home_page.ShopItems().click()

        checkout_page = CheckoutPage(self.driver)
        log.info("Getting all card titles")
        list_of_all_mob = checkout_page.getCards()

        # for mob in list_of_all_mob:
        #     if mob.find_element_by_xpath("div/h4/a").text == "Blackberry":
        #         mob.find_element_by_xpath("div[@class='card-footer']/button").click()

        for mob in list_of_all_mob:
            if checkout_page.getCardName(mob).text == "Blackberry":
                checkout_page.getCardFooterButton(mob).click()


        # self.driver.find_element_by_class_name("nav-link.btn.btn-primary").click()
        checkout_page.getCardFooter().click()

        self.driver.find_element_by_class_name("btn.btn-success").click()
        log.info("Entering country name")
        self.driver.find_element_by_css_selector("#country").send_keys("India")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_all_elements_located((By.LINK_TEXT, "India")))
        self.verify_link_presence("India")

        self.driver.find_element_by_xpath("//a[text()='India']").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("input[type='submit']").click()
        text1 = self.driver.find_element_by_css_selector(".alert-success").text
        log.info("Text received from application is " + text1)
        assert "Success" in text1

        self.driver.get_screenshot_as_file("shubham.png")

        self.driver.close()
