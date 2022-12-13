"""
Functions to manage the sidebar.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By


def select_tab(tab_name: str, driver: webdriver.Chrome):
    """
    Select the tab with the given name from the sidebar
    """
    driver.find_element(
        By.CSS_SELECTOR, f"#sidebar [data-tab='{tab_name}']").click()
