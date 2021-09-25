import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verify_link_presence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_all_elements_located((By.LINK_TEXT, text)))

    def select_gender(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s : %(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)  # File handler object given at this point

        logger.setLevel(logging.DEBUG)
        return logger
