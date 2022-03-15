import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from base.BaseDriver import Base_driver


class Result(Base_driver):
    def __init__(self, driver):
        super().__init__(driver, wait)
        self.driver = driver
        # self.wait = wait

    FILTER_OF_ONE_STOP = "//p[text()=1]"
    FILTER_OF_TWO_STOPS = "//p[text()=2]"
    FILTER_OF_NON_STOP = "//p[text()=0]"

    def get_filter_by_one_stop(self):
        return self.driver.find_element_by_xpath(self.FILTER_OF_ONE_STOP)

    def get_filter_by_two_stops(self):
        return self.driver.find_element_by_xpath(self.FILTER_OF_TWO_STOPS)

    def get_filter_by_Nonstop(self):
        return self.driver.find_element_by_xpath(self.FILTER_OF_NON_STOP)

    def filter_by_stop(self, by_stop):
        if by_stop == '1 Stop':
            self.get_filter_by_one_stop().click()
            print("selected filter is having 1 stop")
            stop = self.driver.find_element_by_xpath("//span[text()='1']")
            if stop.text == '1':
                assert True
                print(stop.text + 'stop')

            time.sleep(3)
        elif by_stop == '2 Stops':
            self.get_filter_by_two_stops().click()
            print("selected filter is having 2 stops")
            stop = self.driver.find_element_by_xpath("//span[text()='2']")
            if stop.text == '2':
                assert True
                print(stop.text + 'stops')

            time.sleep(3)

        elif by_stop == 'Non Stop':
            self.get_filter_by_Nonstop().click()
            print('selected filter is having Nonstops')
            stop = self.driver.find_element_by_xpath("//span[text()='0']")
            if stop.text == '0':
                assert True
                print(stop.text + 'stops')

            time.sleep(3)
        else:
            print("click correct filter")
            time.sleep(3)


