import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pickle
from mskrap import *
import os



browser=webdriver.Chrome(executable_path='/home/mateusz/pyton/chromedriver')
browser.maximize_window()
browser.get('https://www.facebook.com/?sk=h_chr')
email = os.environ.get("EMAIL")
haslo = os.environ.get("PASSE")
input("Wciśnij enter aby kontynuować...")
browser.find_element_by_id("email").send_keys(email)
browser.find_element_by_id("pass").send_keys(haslo)
input("Zaloguj i zamknij pop-up. Wciśnij enter aby kontynuować...")
#browser.find_element_by_name("login").click()
x = Skrap()


def scrolling(link):
    browser.get(link)
    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(0.5)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        try:
            browser.find_element_by_css_selector('div[class="_4vpk"]')
            # Wyniki spoza zakresu wyszukiwania
            break
        except:
            pass

        if new_height == last_height:
            break
        last_height = new_height
    print("Zakończono przewijanie strony.")
    return browser.page_source

def wyciaganie_danych(page_source):
    divs = BeautifulSoup(page_source,"html.parser").find_all("div",{"class":"b3onmgus ph5uu5jm g5gj957u buofh1pr cbu4d94t rj1gh0hx j83agx80 rq0escxv fnqts5cd fo9g3nie n1dktuyu e5nlhep0 ecm0bbzt"})
    for i in divs:
        try:
            price = i.find("div",{"class":"hlyrhctz"}).get_text().rstrip(" zł").replace(u'\xa0', '')
            if price.upper() == "BEZPŁATNE":
                price = 0
            price = int(price)
            link = '<p align="center"><b><a href="https://www.facebook.com/' + str(i.find('a')['href'])+'">Zobacz aukcje.</a></b></p>'
            div = str(i) + f'<h3 align="center">{price}</h3><br />'
            Skrap.diwy.append((div, price, link))
        except:
            pass


def tworzenie_strony(diwy_cena):
    diwy_cena.sort(key=lambda x: x[1])
    with open("fb.html", "w") as f:
        f.write('<body style="background-color:#808080;">')
        for x, i in enumerate(diwy_cena):
            f.write(f'<p>{x}</p>')
            f.write(i[0])
            f.write(f'<p><b><a href="{i[2]}"> Link </a></b></p>')
        f.write('</body>')
    print("Zapisano: ",len(diwy_cena), " ogłoszeń.")

def skrap_other(url):
    if "olx" in url:
        divs = get_divs(*get_range(url))
        for x in divs:
            cena = int(x.find('p', {"class": "price"}).text.replace("\n", "").replace(" ", "")[:-2].split(",")[0])
            link = x.find("h3").find('a')['href']
            diwy_cena.append((str(x), cena, link))
    elif "otomoto" in url:
        divs = otoget_divs(*otoget_range(url))
        for x in divs:
            cena = int(x.find("span", {"class":"offer-price__number ds-price-number"}).find("span").get_text().split(",")[0].replace(" ",""))
            link = x.find("h2").find("a")['href']
            diwy_cena.append((str(x), cena, link))

def get_range(url):
    r=requests.get(url)
    c=r.content
    page= str(BeautifulSoup(c,"html.parser").find_all("script"))
    index=page.index("page_count")
    z=[i for i in page[index+12:index+18] if i.isdigit() ]
    return int("".join(z)), url

def get_divs(num, url):
    r=requests.get(url+"&page="+str(num))
    c=r.content
    return BeautifulSoup(c,"html.parser").find_all("div",{"class":"offer-wrapper"})

def otoget_range(url):
    r=requests.get(url)
    c=r.content
    page= str(BeautifulSoup(c,"html.parser").find_all("noscript"))
    index = page.split("page_count=")[1][:3]
    z=[i for i in index if i.isdigit() ]
    return int("".join(z)), url

def otoget_divs(num, url):
    r=requests.get(url+"&page="+str(num))
    c=r.content
    return BeautifulSoup(c,"html.parser").find_all("article",{"class":"adListingItem offer-item is-row is-active ds-ad-card-experimental"})

def zapis(divs):
    pickle_out = open("fb.pickle", "wb")
    pickle.dump(divs, pickle_out)
    pickle_out.close()

def odczyt():
    pickle_in = open("fb.pickle", "rb")
    return pickle.load(pickle_in)

def porownywanie_list(diwy1, diwy2):
    a = set(diwy1)
    b = set(diwy2)
    return list(a-b)

#diwy_cena = []
#odczytane = odczyt()
#
#input("Zamknij pop-up. Wciśnij enter aby kontynuować...")
#print("Scrollowanie...")
#
link = "https://www.facebook.com/marketplace/108131525886841/motorcycles"
link2 = "https://www.facebook.com/marketplace/108131525886841/search/?query=bmw&maxPrice=25000&categoryID=vehicles&radiusKM=100&vertical=C2C&sort=BEST_MATCH"
wyciaganie_danych(scrolling(link))
x.create_website(0)
#print("OLX: BMW")
#skrap_other("https://www.olx.pl/motoryzacja/samochody/bmw/radzyn-podlaski/?search%5Bfilter_float_price%3Ato%5D=25000&search%5Bfilter_float_enginepower%3Afrom%5D=150&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_enum_transmission%5D%5B0%5D=manual&search%5Border%5D=filter_float_price%3Aasc&search%5Bdist%5D=100")
#print("Omega")
#skrap_other("https://www.olx.pl/motoryzacja/samochody/opel/omega/radzyn-podlaski/?search%5Bfilter_float_price%3Ato%5D=25000&search%5Bfilter_float_enginepower%3Afrom%5D=150&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_enum_transmission%5D%5B0%5D=manual&search%5Border%5D=filter_float_price%3Aasc&search%5Bdist%5D=100")
#print("Merc")
#skrap_other("https://www.olx.pl/motoryzacja/samochody/mercedes-benz/radzyn-podlaski/?search%5Bfilter_float_price%3Ato%5D=25000&search%5Bfilter_float_enginepower%3Afrom%5D=150&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_enum_transmission%5D%5B0%5D=manual&search%5Bdist%5D=100")
#print("Lexus")
#skrap_other("https://www.olx.pl/motoryzacja/samochody/lexus/radzyn-podlaski/?search%5Bfilter_float_price%3Ato%5D=25000&search%5Bfilter_enum_transmission%5D%5B0%5D=manual&search%5Border%5D=filter_float_price%3Aasc&search%5Bdist%5D=100")
#print("OTOMOTO: BMW")
#skrap_other("https://www.otomoto.pl/osobowe/bmw/seg-sedan/radzyn-podlaski/?search%5Bfilter_float_price%3Ato%5D=25000&search%5Bfilter_float_engine_power%3Afrom%5D=150&search%5Bfilter_enum_gearbox%5D%5B0%5D=manual&search%5Bfilter_enum_gearbox%5D%5B1%5D=manual-sequential&search%5Border%5D=filter_float_price%3Aasc&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bdist%5D=100&search%5Bcountry%5D=")
#print("Omega")
#skrap_other("https://www.otomoto.pl/osobowe/opel/omega/seg-sedan/radzyn-podlaski/?search%5Bfilter_float_price%3Ato%5D=25000&search%5Bfilter_enum_gearbox%5D%5B0%5D=manual&search%5Bfilter_enum_gearbox%5D%5B1%5D=manual-sequential&search%5Border%5D=filter_float_price%3Aasc&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bdist%5D=100&search%5Bcountry%5D=")
#print("Merc")
#skrap_other("https://www.otomoto.pl/osobowe/mercedes-benz/seg-sedan/radzyn-podlaski/?search%5Bfilter_float_price%3Ato%5D=25000&search%5Bfilter_float_engine_power%3Afrom%5D=150&search%5Bfilter_enum_gearbox%5D%5B0%5D=manual&search%5Bfilter_enum_gearbox%5D%5B1%5D=manual-sequential&search%5Border%5D=filter_float_price%3Aasc&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bdist%5D=100&search%5Bcountry%5D=")
#print("Lexus")
#skrap_other("https://www.otomoto.pl/osobowe/lexus/is/radzyn-podlaski/?search%5Bfilter_float_price%3Ato%5D=25000&search%5Bfilter_enum_gearbox%5D%5B0%5D=manual&search%5Bfilter_enum_gearbox%5D%5B1%5D=manual-sequential&search%5Border%5D=filter_float_price%3Aasc&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bdist%5D=100&search%5Bcountry%5D=")
#
#nowe = porownywanie_list(diwy_cena, odczytane)
#tworzenie_strony(nowe)
#diwy_cena.extend(nowe)
#zapis(diwy_cena)
#
## selenium
## link = divy[0].find_element_by_tag_name('a').get_attribute('href')
## cena = divy[0].find_element_by_css_selector('div[class="_f3l _4x3g"]').text.rstrip(' zł')
## browser.find_element_by_id("link-next").click()
## browser.save_screenshot(str(i) + '.png')
#
## bs4
## link = x[0].find('a')['href']
## price = x[0].find("div",{"class":"_f3l _4x3g"}).get_text().rstrip(" zł")
#