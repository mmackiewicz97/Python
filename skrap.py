#!/usr/bin/env python
# coding: utf-8
import requests, re
import folium
import sqlite3
from geopy.geocoders import ArcGIS
from bs4 import BeautifulSoup

nom = ArcGIS()

sql = sqlite3.connect("/home/mateusz/Pobrane/baz.sql")
db = sql.cursor()

map = folium.Map(location=[52.2258014,21.0078177], zoom_start=6)
#def soup(motor,num):
#    r=requests.get("https://www.olx.pl/motoryzacja/motocykle-skutery/q-"+str(motor)+"/?page="+str(num))
#    c=r.content
#    return BeautifulSoup(c,"html.parser")
def soup(num):
    r=requests.get("https://www.olx.pl/motoryzacja/motocykle-skutery/radzyn-podlaski/?search%5Bfilter_float_price%3Ato%5D=7000&search%5Bfilter_float_enginesize%3Afrom%5D=600&search%5Border%5D=created_at%3Adesc&search%5Bdist%5D=250&page="+str(num))
    c=r.content
    return BeautifulSoup(c,"html.parser")

def get_range(soup):
    page=str(soup.find_all("script"))
    index=page.index("page_count")
    z=[i for i in page[index+12:index+18] if i.isdigit() ]
    return int("".join(z))

q='SELECT adres FROM moto'
z=db.execute(q)
for i in z.fetchall():
    print(i[0])
q = 'CREATE TABLE IF NOT EXISTS moto (link TEXT, opis TEXT, cena TEXT , adres TEXT)'
db.execute(q)

stron = get_range(soup(1))
print("znaleziono {} stron".format(stron))

for i in range(1,stron+1):
    strona=soup(i)
    all=strona.find_all("div",{"class":"offer-wrapper"})
    print(i," strona")
    for x in all:
        link=x.find("h3").find('a')['href']
        opis=x.find("h3").text.replace("\n","").replace('"',"")
        cena=x.find('p',{"class":"price"}).text.replace("\n","")
        adres=x.find('i',{"data-icon":"location-filled"}).parent.get_text().replace("\n","").replace("  ","")
        query=f'INSERT INTO moto (link, opis, cena, adres) VALUES ("{link}", "{opis}","{cena}", "{adres}")'
        db.execute(query)

def koordynaty(miejscowosc, timeout=0, x=0):
    try:
        return nom.geocode(miejscowosc,timeout=timeout)[1]
    except GeocoderTimedOut:
        x+=1
        if x==10:
            raise ValueError('A very specific bad thing happened.')
        else:
            return koordynaty(miejscowosc,timeout, x)

q='CREATE TABLE IF NOT EXISTS koordynaty (adres, x, y)'
db.execute(q)
    
print("Zbieranie koordynat")
q='SELECT adres FROM moto GROUP BY adres'
z=db.execute(q)
for i in z.fetchall():
    x,y=koordynaty(i[0])
    q=f'INSERT INTO koordynaty (adres, x, y) VALUES ("{i[0]}", "{x}", "{y}")'
    db.execute(q)

print("Umieszczanie danych na mapie")
q='SELECT m.adres, k.x, k.y FROM moto m, koordynaty k WHERE m.adres=k.adres GROUP BY m.adres HAVING COUNT(m.link)>1 '
z=db.execute(q)
for i in z.fetchall():
    q=f'SELECT m.link, m.opis, m.cena FROM moto m, koordynaty k WHERE m.adres = "{i[0]}" AND k.adres = "{i[0]}"'
    z=db.execute(q)
    ahref=""
    for j in z.fetchall():
        ahref+='<a href="{}">{} {}</a><br>'.format(j[0], j[1], j[2])
    folium.Marker([float(i[1]),float(i[2])], popup=ahref).add_to(map)
q='SELECT k.x, k.y, m.link, m.opis, m.cena FROM koordynaty k, moto m WHERE k.adres = m.adres AND m.adres IN (SELECT adres FROM moto GROUP BY adres HAVING COUNT(link)=1)'
z=db.execute(q)
for i in z.fetchall():
    folium.Marker([float(i[0]),float(i[1])], popup='<a href="'+i[2]+'">'+i[3]+" "+i[4]+'</a>').add_to(map)

map.save("Mapa.html")
sql.commit()
sql.close()
print("Zakończono pomyślnie")
