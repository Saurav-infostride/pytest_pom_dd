import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
import allure
import pytest
from logging import critical
from allure_commons.types import AttachmentType
from Tests.test_Base import BaseTest
from Config.config import TestData
from Pages.LoginPage import LoginPage 

class Test_Login(BaseTest):

    @pytest.mark.order(1)
    def test_verify_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.JPG)

    @pytest.mark.order(2)
    def test_verify_login_into_app(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.JPG)

