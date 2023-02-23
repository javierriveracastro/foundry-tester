"""
Main history file to test BR2
"""

from test_api.side_bar import select_tab, open_actor, clear_chat
from test_api.swade import roll_attribute


def run_history(web_driver):
    """
    Runs the history
    """
    clear_chat(web_driver)
    select_tab('actors', web_driver)
    open_actor('Turnling', 'Personajes', web_driver)
    roll_attribute('agility', web_driver)
