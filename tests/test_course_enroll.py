import pytest
from pages.course_page import CoursePage

@pytest.mark.usefixtures("setup")
class TestCourseEnroll:
    def test_enroll_in_course(self):
        self.driver.get("https://opencart.abstracta.us/")

        course = CoursePage(self.driver)
        course.enroll_in_course("MacBook")

        success_msg = course.get_success_message()

        assert "Success: You have added MacBook" in success_msg
