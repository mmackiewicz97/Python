from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

browser=webdriver.Firefox()

browser.get('https://play2048.co/')

game = browser.find_element_by_class_name('game-container').click()
grid = browser.find_element_by_tag_name('body')
direction = {0: Keys.UP, 1: Keys.RIGHT, 2: Keys.DOWN, 3: Keys.LEFT}
count=0
while True:
    grid.send_keys(direction[count%4])
    count+=1
    time.sleep(0.1)
    try:
        WebDriverWait(browser, .00001).until(EC.presence_of_element_located((By.ID, "game-message game-over")))
        browser.find_element_by_class_name('retry-button').click()
        browser.save_screenshot('screen.png')
    except:
        pass
