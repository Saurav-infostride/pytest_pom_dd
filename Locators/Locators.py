from selenium.webdriver.common.by import By

class Locators:
    HEADER = (By.XPATH, "//span[@class='title']")
    TWITTER_LINK = (By.XPATH, "//*[@class='social_twitter']")
    CART_ICON = (By.XPATH, "//a[@class='shopping_cart_link']")

    EMAIL = (By.XPATH, "//input[@id='user-name']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")