"""
Functions to manage the sidebar.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond

from src.settings import SMALL_TIMEOUT_SECONDS


def select_tab(tab_name: str, driver: webdriver.Chrome):
    """
    Select the tab with the given name from the sidebar
    """
    driver.find_element(
        By.CSS_SELECTOR, f"#sidebar [data-tab='{tab_name}']").click()
    contenido = driver.find_element(By.ID, tab_name)
    WebDriverWait(driver, SMALL_TIMEOUT_SECONDS).until(
        cond.visibility_of(contenido))
