"""
Opens and test a foundry install
"""

import os
import time
import subprocess

from settings import FOUNDRY_BIN_DIR, FOUNDRY_DATA_DIR

if __name__ == '__main__':
    os.chdir(FOUNDRY_BIN_DIR)
    print("Starting Foundry")
    foundry_process = subprocess.Popen(
        ['node', 'resources/app/main.js', f'--dataPath={FOUNDRY_DATA_DIR}'])
    time.sleep(10)
    print("Foundry Running")
    foundry_process.terminate()
    try:
        foundry_process.wait(20)
    except subprocess.TimeoutExpired:
        foundry_process.kill()
    print("Foundry stopped")