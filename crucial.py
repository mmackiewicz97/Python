import requests, re
from bs4 import BeautifulSoup
import webbrowser

r=requests.get("https://www.morele.net/komputery/podzespoly-komputerowe/dyski-ssd-518/,,,,,,,p,0,,,,15254O!2842/1/")
c=r.content

soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div", {"class":"cat-product-content"})
if int(all[0].find("div", {"class","price-new"}).contents[0][:3])<120:
    webbrowser.open("https://www.morele.net"+all[0].find("a")['href'], new=2)
    webbrowser.open("https://www.morele.net/komputery/podzespoly-komputerowe/dyski-ssd-518/,,,,,,,p,0,,,,15254O!2842/1/")
#for i in all:
#    print('https://www.morele.net/'+i.find("a")['href'])
#    print(i.find("div", {"class","price-new"}).contents[0])
