import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
import allure
from Tests.test_Base import BaseTest
from Config.config import TestData
from Pages.LoginPage import LoginPage 

@allure.severity(allure.severity_level.NORMAL)
class Test_Login(BaseTest):

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login_into(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login()
        time.sleep(5)

