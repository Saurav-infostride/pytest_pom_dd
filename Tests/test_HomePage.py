import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
import allure 
from allure_commons.types import AttachmentType
from Tests.test_Base import BaseTest
from Config.config import TestData
from Pages.LoginPage import LoginPage

class Test_Home(BaseTest):

    @pytest.mark.order(1)
    def test_verify_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        title = homePage.get_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.JPG)

    @pytest.mark.order(2)
    def test_verify_home_page_header(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        header = homePage.get_header_value()
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.JPG)
        assert header == TestData.HOME_PAGE_HEADER

    @pytest.mark.order(3)
    def test_verify_cart_icon_visible(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        notification = homePage.is_cart_icon_exist()
        assert notification
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.JPG)

    @pytest.mark.order(4)
    @pytest.mark.skip
    def test_verify_twitter_icon_visible(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        twitter = homePage.is_twitter_icon_exist()
        assert twitter
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.JPG)