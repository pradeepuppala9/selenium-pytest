import pytest
from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# making this setup method available for class = scope.
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # wait = WebDriverWait(driver, 20)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()

    request.cls.driver = driver
    # request.cls.wait = wait
    yield
    time.sleep(10)
    driver.close()
