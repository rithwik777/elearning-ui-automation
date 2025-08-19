from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class CoursePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "search")
        self.search_button = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")
        self.course_link = (By.LINK_TEXT, "MacBook")
        self.add_to_cart_button = (By.ID, "button-cart")
        self.success_message = (By.CSS_SELECTOR, "div.alert-success")

    def enroll_in_course(self, course_name="MacBook"):
        # Search course
        self.driver.find_element(*self.search_box).send_keys(course_name)
        self.driver.find_element(*self.search_button).click()

        # Click course
        self.driver.find_element(*self.course_link).click()

        # Enroll (Add to Cart)
        self.driver.find_element(*self.add_to_cart_button).click()
        time.sleep(2)  # wait for message

    def get_success_message(self):
        return self.driver.find_element(*self.success_message).text
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class CoursePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "search")
        self.search_button = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")
        self.course_link = (By.LINK_TEXT, "MacBook")
        self.add_to_cart_button = (By.ID, "button-cart")
        self.success_message = (By.CSS_SELECTOR, "div.alert-success")

    def enroll_in_course(self, course_name="MacBook"):
        # Search course
        self.driver.find_element(*self.search_box).send_keys(course_name)
        self.driver.find_element(*self.search_button).click()

        # Click course
        self.driver.find_element(*self.course_link).click()

        # Enroll (Add to Cart)
        self.driver.find_element(*self.add_to_cart_button).click()
        time.sleep(2)  # wait for message

    def get_success_message(self):
        return self.driver.find_element(*self.success_message).text
