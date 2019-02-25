from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

browser=webdriver.Firefox()

#browser.get('https://pl4.forgeofempires.com/game/index?ref=')
browser.get('file:///home/mateusz/Rasp/click.html')
#browser.find_element_by_id("login_userid").send_keys('mati1058@interia.pl')
#browser.find_element_by_id("login_password").send_keys('1997Matlandia')
#browser.find_element_by_id("login_Login").click()
#time.sleep(4)
#browser.find_element_by_class_name("play_button").click()
#browser.find_element_by_link_text("Dinegu").click()
#time.sleep(30)
actions = webdriver.ActionChains(browser)
body = browser.find_element_by_tag_name("body")
actions.move_to_element_with_offset(body,1132, 41).click().perform()
time.sleep(2)
x = 1
while True:
    print("Pętla nr: ", x)
    x+=1
    actions.move_to_element_with_offset(body,642, 164).click().perform()
    time.sleep(2)
    actions.move_to_element_with_offset(body,642, 164).click().perform()
    time.sleep(3)
    actions.move_to_element_with_offset(body,428,309).click().perform()

    time.sleep(2)
    actions.move_to_element_with_offset(body,463,247).click().perform()
    time.sleep(2)
    actions.move_to_element_with_offset(body,463,247).click().perform()
    time.sleep(3)
    actions.move_to_element_with_offset(body,428,309).click().perform()

    time.sleep(2)
    actions.move_to_element_with_offset(body,582,303).click().perform()
    time.sleep(2)
    actions.move_to_element_with_offset(body,582,303).click().perform()
    time.sleep(3)
    actions.move_to_element_with_offset(body,428,309).click().perform()

    time.sleep(2)
    actions.move_to_element_with_offset(body,657,345).click().perform()
    time.sleep(2)
    actions.move_to_element_with_offset(body,657,345).click().perform()
    time.sleep(3)
    actions.move_to_element_with_offset(body,428,309).click().perform()
    time.sleep(300)

#actions.move_by_offset(428, 300).click().perform()
#browser.find_element_by_class_name("world_select_button").click()
#game = browser.find_element_by_class_name('game-container').click()
#grid = browser.find_element_by_tag_name('body')
#direction = {0: Keys.UP, 1: Keys.RIGHT, 2: Keys.DOWN, 3: Keys.LEFT}
#count=0
#while True:
#    grid.send_keys(direction[count%4])
#    count+=1
#    time.sleep(0.1)
#    try:
#        WebDriverWait(browser, .00001).until(EC.presence_of_element_located((By.ID, "game-message game-over")))
#        browser.find_element_by_class_name('retry-button').click()
#        browser.save_screenshot('screen.png')
#    except:
#        pass
