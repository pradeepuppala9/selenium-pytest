from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base_driver:
    def __init__(self, driver,wait):
        self.driver = driver
        self.wait = wait

# we can also add methods like scrolling pages
    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        clickable_element = wait.until(
            EC.element_to_be_clickable(
                (locator_type, locator)))
        return clickable_element

    def wait_until_elements_are_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        locatable_element = wait.until(
            EC.presence_of_all_elements_located(
                (locator_type, locator)))
        return locatable_element


