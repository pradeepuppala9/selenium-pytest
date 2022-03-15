import time

import ddt
import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from pages.yatra_launch_page import LaunchPage
from pages.result import Result
#from ddt import ddt,data,unpack


@pytest.mark.usefixtures("setup")
#@ddt
class Test_Demo:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)

    #@data("New Delhi", "JFK", "15/04/2022","1 Stop")
    '''def test_Demo_result_by_Nonstop(self,from_location,to_location,date,stops):
        search_flight_object = self.lp.search_flights_method(from_location,to_location,date)
        search_flight_object.filter_by_stop(stops)'''

    def test_Demo_result_by_one_stop(self):
        search_flight_object = self.lp.search_flights_method("New Delhi", "JFK", "15/04/2022")
        search_flight_object.filter_by_stop('2 Stops')
