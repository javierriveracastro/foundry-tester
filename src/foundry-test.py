"""
Opens and test a foundry install
"""

import os
import time
import subprocess

from selenium import webdriver

from settings import FOUNDRY_BIN_DIR, FOUNDRY_DATA_DIR


def close_test(open_driver, open_foundry_proc):
    """
    Closes the webdriver and the Foundry instance as clean as possible
    """
    open_driver.quit()
    open_foundry_proc.terminate()
    try:
        open_foundry_proc.wait(20)
    except subprocess.TimeoutExpired:
        open_foundry_proc.kill()
    print("Foundry stopped")


def start_webdriver():
    """
    Create the webdriver instance and point it to foundry
    :return: a webdriver instance
    """
    driver = webdriver.Chrome()
    driver.get("http://localhost:30000")
    time.sleep(10)
    return driver


if __name__ == '__main__':
    os.chdir(FOUNDRY_BIN_DIR)
    print("Starting Foundry")
    foundry_process = subprocess.Popen(
        ['node', 'resources/app/main.js', f'--dataPath={FOUNDRY_DATA_DIR}'])
    time.sleep(10)
    print("Foundry Running")
    web_driver = start_webdriver()
    close_test(web_driver, foundry_process)
