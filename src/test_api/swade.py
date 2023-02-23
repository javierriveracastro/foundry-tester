"""
API for the SWADE system
"""

from selenium.webdriver.common.by import By

from .side_bar import select_tab


def click_attribute(name, driver):
    """
    Rolls an attribute
    :param name: Name of the attribute
    :param driver: Selenium driver
    """
    select_tab('chat', driver)
    attribute_button = None
    for button in driver.find_elements(
            By.CSS_SELECTOR, "button.attribute-value"):
        if button.get_attribute('data-attribute') == name:
            attribute_button = button
            break
    if attribute_button:
        attribute_button.click()

