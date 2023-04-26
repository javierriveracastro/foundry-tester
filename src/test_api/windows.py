"""
API for managing Foundry Windows
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def close_all_windows(driver: webdriver.Chrome):
    """
    Closes all open windows
    :param driver: Selenium driver
    """
    for close_button in driver.find_elements(By.CSS_SELECTOR,
                                             '.header-button.close'):
        time.sleep(1)  # I have no idea why I need to wait here...
        close_button.click()


def wait_for_notification_close(driver: webdriver.Chrome):
    """
    Waits for a notification to close
    :param driver: Selenium driver
    """
    for notification in driver.find_elements(
            By.CSS_SELECTOR, 'li.notification'):
        notification.find_element(By.CSS_SELECTOR, '.close').click()
