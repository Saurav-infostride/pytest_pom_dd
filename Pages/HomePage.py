import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Pages.BasePage import BasePage
from Locators.Locators import Locators

class HomePage(BasePage):

    '''constructor of the page class'''
    def __init__(self, driver):
        super().__init__(driver)

    '''Page Actions for home page'''
    '''this method is use to get the page title'''
    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_cart_icon_exist(self):
        return self.is_visible(Locators.CART_ICON)

    def get_header_value(self):
        return self.get_element_text(Locators.HEADER)

    def is_twitter_icon_exist(self):
        return self.is_visible(Locators.TWITTER_LINK)