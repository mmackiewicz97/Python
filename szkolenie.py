from selenium import webdriver
import time
import random
import os

browser=webdriver.Chrome(executable_path='..\\chromedriver.exe')

browser.get('https://elearning.straz.lublin.pl/')
browser.find_element_by_id("f_login").send_keys('login')
browser.find_element_by_id("f_password").send_keys('haslo')
browser.find_element_by_name("btnSignIn").click()

def info(l):
    #print("Link:")
    link = l
    if not link.endswith("index.html"):
        link = link.replace('info', 'index')
    return link

def szkolenie(link):
    browser.get(link)
    time.sleep(3)
    page = browser.find_element_by_css_selector('div[class="slide-counter test"]')
    strony = int(page.text.split('/')[1])
    for i in range(1, strony):
        browser.find_element_by_id("link-next").click()
        print(i)
        #browser.get(link.replace('index', 'index,'+str(i)))
        #browser.save_screenshot(str(i) + '.png')
        time.sleep(random.randint(3,50))
    browser.find_element_by_id("link-finish").click()
    print("Ukończono: "+link)
    print(time.localtime())
    browser.find_element_by_css_selector(
        "button[class='saveButtonClass ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only']").click()
    time.sleep(5)
lista = []
for x in lista:
    szkolenie(info(x))