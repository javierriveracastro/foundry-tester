"""
Main history file to test BR2
"""

from test_api.side_bar import select_tab


def run_history(web_driver):
    """
    Runs the history
    """
    select_tab('actors', web_driver)
