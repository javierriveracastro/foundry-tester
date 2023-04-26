"""
API for the BR2 module
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

from .side_bar import get_last_message


def roll_last_card_trait(driver: webdriver.Chrome):
    """
    Clicks the roll button of the last card clicked
    :param driver: Selenium driver
    """
    chat_message = get_last_message(driver)
    chat_message.find_element(By.CSS_SELECTOR, ".brsw-roll-button").click()


