"""
Opens and test a foundry install
"""

import os
import time
import subprocess
import importlib

from selenium import webdriver

from settings import FOUNDRY_BIN_DIR, FOUNDRY_DATA_DIR, TEST_WORLD, \
    GM_PASSWORD, SMALL_TIMEOUT_SECONDS, HISTORY
from test_api.launching import open_world, launch_world

from test_api.side_bar import select_tab

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
    driver.implicitly_wait(SMALL_TIMEOUT_SECONDS)
    driver.get("http://localhost:30000")
    time.sleep(SMALL_TIMEOUT_SECONDS)
    return driver


if __name__ == '__main__':
    os.chdir(FOUNDRY_BIN_DIR)
    print("Starting Foundry")
    foundry_process = subprocess.Popen(
        ['node', 'resources/app/main.js', f'--dataPath={FOUNDRY_DATA_DIR}'])
    time.sleep(SMALL_TIMEOUT_SECONDS)
    print("Foundry Running")
    history = importlib.import_module(f'histories.{HISTORY}')
    web_driver = start_webdriver()
    open_world(TEST_WORLD, web_driver)
    launch_world(GM_PASSWORD, web_driver)
    select_tab('actors', web_driver)
    history.run_history(web_driver)
    js_errors = [log['message'] for log in web_driver.get_log('browser')
                 if log['level'] == 'SEVERE']
    close_test(web_driver, foundry_process)
    if js_errors:
        print("JS Errors:")
        for error in set(js_errors):
            print(error)
