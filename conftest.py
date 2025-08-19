import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

@pytest.fixture(scope="class")
def setup(request):
    # Path to chromedriver inside project folder
    driver_path = os.path.join(os.getcwd(), "chromedriver.exe")

    options = Options()
    options.add_argument("--start-maximized")

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

    request.cls.driver = driver
    yield
    driver.quit()
