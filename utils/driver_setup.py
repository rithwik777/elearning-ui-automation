from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.add_argument("--start-maximized")
    service = Service("chromedriver.exe")  # Update path if needed
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()
