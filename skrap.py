#!/usr/bin/env python
# coding: utf-8
from geopy.exc import GeocoderTimedOut
import requests, re
import folium
import sqlite3
from geopy.geocoders import ArcGIS
from bs4 import BeautifulSoup
import os 

nom = ArcGIS()
class Skrap:
    diwy = []
    def __init__(self, url):
        #self.moto = moto
        self.baza="baza.sql"
        self.sql = sqlite3.connect(self.baza)
        self.db = self.sql.cursor()
        self.map = folium.Map(location=[52.2258014,21.0078177], zoom_start=6)
        q = 'CREATE TABLE IF NOT EXISTS moto (link TEXT, opis TEXT, cena TEXT , adres TEXT)'
        self.db.execute(q)
        self.url=url
        self.insert()
        #self.set_address()
        #self.set_markers()

    def get_divs(self,num):
        r=requests.get(self.url+"&page="+str(num))
#        r=requests.get("https://www.olx.pl/motoryzacja/motocykle-skutery/q-{}/?page={}".format(self.moto,str(num)))
        c=r.content
        return BeautifulSoup(c,"html.parser").find_all("div",{"class":"offer-wrapper"})

    def get_div_address(self,url):
        '''Trzeba uwazac na bana od olx 
        lub otomoto'''
        r=requests.get(url)
        c=r.content
        if "olx" in url:
            return BeautifulSoup(c,"html.parser").find("a",{"class":"show-map-link"}).get_text()
        else:
            return BeautifulSoup(c,"html.parser").find("span",{"class":"seller-box__seller-address__label"}).get_text().strip()

    def get_range(self):
        r=requests.get(self.url)
        #r=requests.get("https://www.olx.pl/motoryzacja/motocykle-skutery/q-{}/?page=1".format(self.moto))
        c=r.content
        page= str(BeautifulSoup(c,"html.parser").find_all("script"))
        index=page.index("page_count")
        z=[i for i in page[index+12:index+18] if i.isdigit() ]
        return int("".join(z))

    def insert(self):
        x = self.get_range()
        print(x, "stron")
        for i in range(1,x+1):
            print(i, "strona")
            for x in self.get_divs(i):
                link=x.find("h3").find('a')['href']
                opis=x.find("h3").text.replace("\n","").replace('"',"")
                opis =re.sub('\W+',' ', opis)
                cena=x.find('p',{"class":"price"}).text.replace("\n","")
                #adres=self.get_div_address(link)
                adres=x.find('i',{"data-icon":"location-filled"}).parent.get_text().replace("\n","").replace("  ","")
                #query=f'INSERT INTO moto (link, opis, cena, adres) VALUES ("{link}", "{opis}","{cena}", "{adres}")'
                Skrap.diwy.append((x, int(cena[:-2].replace(" ",""))))
                self.db.execute("INSERT INTO moto (link, opis, cena, adres) VALUES (?,?,?,?)",(link, opis, cena, adres))
        self.sql.commit()

    def koordynaty(self,miejscowosc, timeout=1):
        try:
            return nom.geocode(miejscowosc,timeout=timeout)[1]
        except GeocoderTimedOut:
            timeout+=1
            if timeout == 6:
                raise ValueError('A very specific bad thing happened.')
            else:
                return self.koordynaty(miejscowosc,timeout)

    def set_address(self):
        print("Lokalizowanie...")
        q='CREATE TABLE IF NOT EXISTS koordynaty (adres, x, y)'
        self.db.execute(q)
        q='SELECT adres FROM moto GROUP BY adres'
        z=self.db.execute(q)
        for i in z.fetchall():
            x,y=self.koordynaty(i[0])
            q=f'INSERT INTO koordynaty (adres, x, y) VALUES ("{i[0]}", "{x}", "{y}")'
            self.db.execute(q)
        self.sql.commit()

    def set_markers(self):
        print("Umieszczanie danych na mapie")
        q='SELECT m.adres, k.x, k.y FROM moto m, koordynaty k WHERE m.adres=k.adres GROUP BY m.adres HAVING COUNT(m.link)>1 '
        z=self.db.execute(q)
        for i in z.fetchall():
            q=f'SELECT m.link, m.opis, m.cena FROM moto m, koordynaty k WHERE m.adres = "{i[0]}" AND k.adres = "{i[0]}"'
            z=self.db.execute(q)
            ahref=""
            for j in z.fetchall():
                ahref+='<a href="{}">{} {}</a><br>'.format(j[0], j[1], j[2])
            folium.Marker([float(i[1]),float(i[2])], popup=ahref).add_to(self.map)
        q='SELECT k.x, k.y, m.link, m.opis, m.cena FROM koordynaty k, moto m WHERE k.adres = m.adres AND m.adres IN (SELECT adres FROM moto GROUP BY adres HAVING COUNT(link)=1)'
        z=self.db.execute(q)
        for i in z.fetchall():
            folium.Marker([float(i[0]),float(i[1])], popup='<a href="'+i[2]+'">'+i[3]+" "+i[4]+'</a>').add_to(self.map)
        self.sql.close()
        save = self.baza.split(".")[0]+".html"
        self.map.save(save)
        os.system(f'xdg-open {save}')
        print("Zakończono pomyślnie")

    def create_website(self):
        Skrap.diwy.sort(key=lambda x: x[1])
        with open("olai.html", "w") as f:
            for x, i in enumerate(Skrap.diwy):
                f.write(f'<p>{x}</p>')
                f.write(str(i[0]))
        os.system(f'xdg-open oli.html')
Skrap("https://www.olx.pl/motoryzacja/motocykle-skutery/q-yamaha/?search%5Bfilter_float_price%3Ato%5D=12000&search%5Bfilter_float_year%3Afrom%5D=2004&search%5Bfilter_float_enginesize%3Afrom%5D=600")
### Yamaha fazer
Skrap("https://www.olx.pl/motoryzacja/motocykle-skutery/q-kawasaki/?search%5Bfilter_float_price%3Ato%5D=12000&search%5Bfilter_float_year%3Afrom%5D=2004&search%5Bfilter_float_enginesize%3Afrom%5D=600")
### Kawasaki z750
Skrap("https://www.olx.pl/motoryzacja/motocykle-skutery/q-suzuki/?search%5Bfilter_float_price%3Ato%5D=12000&search%5Bfilter_float_year%3Afrom%5D=2007&search%5Bfilter_float_enginesize%3Afrom%5D=600")
### Suzuki Bandit 
Skrap("https://www.olx.pl/motoryzacja/motocykle-skutery/q-honda/?search%5Bfilter_float_price%3Ato%5D=12000&search%5Bfilter_float_year%3Afrom%5D=2007&search%5Bfilter_float_enginesize%3Afrom%5D=600")
### Honda Hornet
x=Skrap("https://www.olx.pl/motoryzacja/motocykle-skutery/q-sv/?search%5Bfilter_float_price%3Ato%5D=12000&search%5Bfilter_float_year%3Afrom%5D=2003&search%5Bdescription%5D=1&search%5Border%5D=filter_float_price%3Aasc")
## Suzuki Sv
#Skrap("https://www.olx.pl/motoryzacja/motocykle-skutery/radzyn-podlaski/q-yamaha/?search%5Bfilter_float_price%3Ato%5D=12500&search%5Bfilter_float_year%3Afrom%5D=2004&search%5Bfilter_float_enginesize%3Afrom%5D=550&search%5Bdist%5D=250")
#Skrap("https://www.olx.pl/motoryzacja/motocykle-skutery/radzyn-podlaski/q-kawasaki/?search%5Bfilter_float_price%3Ato%5D=12000&search%5Bfilter_float_year%3Afrom%5D=2004&search%5Bfilter_float_enginesize%3Afrom%5D=550&search%5Bdist%5D=250")
#Skrap("https://www.olx.pl/motoryzacja/motocykle-skutery/radzyn-podlaski/q-suzuki/?search%5Bfilter_float_price%3Ato%5D=12000&search%5Bfilter_float_year%3Afrom%5D=2007&search%5Bfilter_float_enginesize%3Afrom%5D=550&search%5Bdist%5D=250")
#Skrap("https://www.olx.pl/motoryzacja/motocykle-skutery/radzyn-podlaski/q-honda/?search%5Bfilter_float_price%3Ato%5D=12000&search%5Bfilter_float_year%3Afrom%5D=2007&search%5Bfilter_float_enginesize%3Afrom%5D=550&search%5Bdist%5D=250")
#x=Skrap("https://www.olx.pl/motoryzacja/motocykle-skutery/radzyn-podlaski/q-sv/?search%5Bfilter_float_price%3Ato%5D=12000&search%5Bfilter_float_year%3Afrom%5D=2003&search%5Bdescription%5D=1&search%5Border%5D=filter_float_price%3Aasc&search%5Bdist%5D=250")
x.create_website()
#x.set_address()
#x.set_markers()
