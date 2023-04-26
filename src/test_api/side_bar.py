"""
Functions to manage the sidebar.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond

from settings import SMALL_TIMEOUT_SECONDS


def select_tab(tab_name: str, driver: webdriver.Chrome):
    """
    Select the tab with the given name from the sidebar
    """
    driver.find_element(
        By.CSS_SELECTOR, f"#sidebar [data-tab='{tab_name}']").click()
    contenido = driver.find_element(By.ID, tab_name)
    WebDriverWait(driver, SMALL_TIMEOUT_SECONDS).until(
        cond.visibility_of(contenido))


def open_actor(name: str, folder: str, driver: webdriver.Chrome):
    """
    Opens the actor with the given name
    """
    if folder:
        folder_element = None
        for icon_element in driver.find_elements(
                By.CSS_SELECTOR, "#sidebar .folder-header h3"):
            if icon_element.text == folder:
                folder_element = icon_element
                break
        if folder_element:
            folder_element.click()
    actor_element = None
    for posible_actor in driver.find_elements(
            By.CSS_SELECTOR, ".directory-item.actor h4"):
        if posible_actor.text == name:
            actor_element = posible_actor
            break
    actor_element.click()


def clear_chat(driver: webdriver.Chrome):
    """
    Clears the chat
    :param driver: Selenium driver
    """
    select_tab('chat', driver)
    driver.find_element(
        By.CSS_SELECTOR, "a.delete.chat-flush .fa-trash").click()
    WebDriverWait(driver, SMALL_TIMEOUT_SECONDS).until(
        lambda drv: drv.find_element(By.CSS_SELECTOR, ".app.dialog"))
    driver.find_element(By.CSS_SELECTOR, ".dialog-button.yes").click()


def get_last_message(driver: webdriver.Chrome):
    """
    Gets the last message in the chat
    :param driver: Selenium driver
    :return: The message
    """
    cards = driver.find_element(By.ID, "chat-log").find_elements(
        By.TAG_NAME, "li")
    return cards[-1] if len(cards) > 0 else None



