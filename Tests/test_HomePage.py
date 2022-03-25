import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import allure
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
from Config.config import TestData

@allure.severity(allure.severity_level.NORMAL)
class Test_Home(BaseTest):

    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        title = homePage.get_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_home_page_header(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        header = homePage.get_header_value()
        assert header == TestData.HOME_PAGE_HEADER

    def test_cart_icon_visible(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        notification = homePage.is_cart_icon_exist()
        assert notification

    def test_twitter_icon_visible(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        twitter = homePage.is_twitter_icon_exist()
        assert twitter