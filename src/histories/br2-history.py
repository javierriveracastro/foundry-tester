"""
Main history file to test BR2
"""

from test_api.side_bar import select_tab, open_actor, clear_chat
from test_api.swade import click_attribute
from test_api.br import roll_last_card_trait
from test_api.windows import close_all_windows, wait_for_notification_close


def run_history(web_driver):
    """
    Runs the history
    """
    clear_chat(web_driver)
    wait_for_notification_close(web_driver)
    select_tab('actors', web_driver)
    open_actor('Turnling', 'Personajes', web_driver)
    click_attribute('agility', web_driver)
    close_all_windows(web_driver)
    roll_last_card_trait(web_driver)
