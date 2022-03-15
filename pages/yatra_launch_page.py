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
from pages.result import Result


class LaunchPage(Base_driver):
    def __init__(self, driver):
        super().__init__(driver, wait)
        self.driver = driver
        # self.wait = wait

    # locators
    DEPART_FROM_FIELD = "flight_origin"
    DEPART_TO_FIELD = "flight_destination"
    SEARCH_RESULTS = "//div[@class='viewport']//div[1]/li"
    BOOKING_DATE = "flight_origin_date"
    ALL_BOOKING_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_FLIGHTS_BUTTON = "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']"

    def get_depart_from_field(self):
        return self.wait_until_element_is_clickable(By.NAME, self.DEPART_FROM_FIELD)

    def get_depart_to_field(self):
        return self.wait_until_element_is_clickable(By.NAME, self.DEPART_TO_FIELD)

    def get_search_results(self):
        return self.wait_until_elements_are_located(By.XPATH, self.SEARCH_RESULTS)

    def get_Booking_date(self):
        return self.wait_until_element_is_clickable(By.NAME, self.BOOKING_DATE)

    def get_All_booking_dates(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ALL_BOOKING_DATES)

    def get_search_flights_results(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SEARCH_FLIGHTS_BUTTON)

    def enterDepartfromlocation(self, departfromlocation):
        self.get_depart_from_field().click()
        self.get_depart_from_field().send_keys(departfromlocation)
        self.get_depart_from_field().send_keys(Keys.ENTER)

    def enterGoingtolocation(self, departtolocation):
        #self.get_depart_to_field().click()
        actions = ActionChains(self.driver)
        actions.double_click(self.get_depart_to_field()).perform()
        time.sleep(5)
        self.get_depart_to_field().send_keys(departtolocation)
        time.sleep(3)

        search_results = self.get_search_results()
        time.sleep(3)
        for results in search_results:
            if departtolocation in results.text:
                results.click()
                break

    def enterDeparturedate(self, departuredate):
        self.get_Booking_date().click()
        all_dates = self.get_All_booking_dates().find_elements(By.XPATH, self.ALL_BOOKING_DATES)

        for date in all_dates:
            if date.get_attribute("id") == departuredate:
                date.click()
                break

    def clicksearchflightsbutton(self):
        self.get_search_flights_results().click()
        time.sleep(5)

    def search_flights_method(self,departfromlocation,departtolocation,departuredate):
        self.enterDepartfromlocation(departfromlocation)
        self.enterGoingtolocation(departtolocation)
        self.enterDeparturedate(departuredate)
        self.clicksearchflightsbutton()
        rp = Result(self.driver)
        return rp


