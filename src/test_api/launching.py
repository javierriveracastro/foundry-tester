import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def open_world(world_name, driver):
    """
    Opens a world in the test environment
    :param world_name:
    :param driver: WebDriver
    """
    warning_close_buttons = driver.find_elements(
        By.CSS_SELECTOR, ".close.fas.fa-times-circle")
    for close_button in warning_close_buttons:
        close_button.click()
    launch_button = driver.find_element(
        By.CSS_SELECTOR,
        f"[data-world='{world_name}'][data-action='launchWorld']")
    launch_button.click()
    driver.find_element(By.NAME, "join")


def launch_world(gm_password: str, driver: webdriver.Chrome):
    """
    Launches a world as gm from the start screen
    """
    user_select = Select(
        driver.find_element(By.CSS_SELECTOR, "[name='userid']"))
    user_select.select_by_index(1)  # We hope the GM is the first user
    driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys(
        gm_password)
    driver.find_element(By.CSS_SELECTOR, "[name='join']").click()
    driver.find_element(By.ID, 'chat-log')
