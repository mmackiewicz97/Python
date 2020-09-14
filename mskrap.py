#!/usr/bin/env python
# coding: utf-8
from geopy.exc import GeocoderTimedOut
import requests, re
import folium
import sqlite3
from geopy.geocoders import ArcGIS
from bs4 import BeautifulSoup
import os 
import time

nom = ArcGIS()
class Skrap:
    diwy = []
    def __init__(self, url=None):
        #self.moto = moto
        self.baza="mbaza.sql"
        self.sql = sqlite3.connect(self.baza)
        self.db = self.sql.cursor()
        self.map = folium.Map(location=[52.2258014,21.0078177], zoom_start=6)
        q = 'CREATE TABLE IF NOT EXISTS moto (link TEXT, opis TEXT, cena INT , adres TEXT, diw TEXT)'
        #q = 'CREATE TABLE IF NOT EXISTS moto (link TEXT, opis TEXT, cena INT , adres TEXT)'
        self.db.execute(q)
        self.url=url
        if url is not None:
            if "olx" in url:
                self.insert()
            elif "otomoto" in url:
                self.otoinsert()
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
        for i in range(1,x+1):
            for x in self.get_divs(i):
                link=x.find("h3").find('a')['href']
                opis=x.find("h3").text.replace("\n","").replace('"',"")
                opis =re.sub('\W+',' ', opis)
                cena=x.find('p',{"class":"price"}).text.replace("\n","").replace(" ","")[:-2].split(",")[0]
                #adres=self.get_div_address(link)
                adres=x.find('i',{"data-icon":"location-filled"}).parent.get_text().replace("\n","").replace("  ","")
                #query=f'INSERT INTO moto (link, opis, cena, adres) VALUES ("{link}", "{opis}","{cena}", "{adres}")'
                q=f'SELECT adres, cena, link, opis FROM moto WHERE adres="{adres}" AND cena="{cena}" AND opis="{opis}"'
                ins = self.db.execute(q)
                if not ins.fetchall():
                    self.db.execute("INSERT INTO moto (link, opis, cena, adres, diw) VALUES (?,?,?,?,?)",(link, opis, cena, adres, str(x)))
                    q=f'SELECT cena, link FROM moto WHERE adres="{adres}" AND opis="{opis}" AND cena!="{cena}"'
                    ins = self.db.execute(q)
                    repeated = ins.fetchall()
                    if repeated:
                        p = ""
                        for i in repeated:
                            p+=f'<a href="{i[1]}">Link</a> <h3 align="right">{i[0]}</h3><br />'
                        Skrap.diwy.append((x, int(cena), p))
                    else:
                        Skrap.diwy.append((x, int(cena)))

                #else:
                #    Skrap.diwy.append((x, int(cena)))
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
        q='SELECT adres FROM moto WHERE adres NOT IN (SELECT adres FROM koordynaty) GROUP BY adres '
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
            folium.Marker([float(i[0]),float(i[1])], popup='<a href="'+i[2]+'">'+i[3]+" "+str(i[4])+' zł</a>').add_to(self.map)
        self.sql.close()
        save = self.baza.split(".")[0]+"map.html"
        self.map.save(save)
        os.system(f'xdg-open {save}')
        print("Zakończono pomyślnie")

    def otoget_divs(self,num):
        r=requests.get(self.url+"&page="+str(num))
        c=r.content
        return BeautifulSoup(c,"html.parser").find_all("article",{"class":"adListingItem offer-item is-row is-active ds-ad-card-experimental"})

    def otoget_range(self):
        r=requests.get(self.url)
        c=r.content
        page= str(BeautifulSoup(c,"html.parser").find_all("noscript"))
        index = page.split("page_count=")[1][:3]
        z=[i for i in index if i.isdigit() ]
        return int("".join(z))
        
    def otoinsert(self):
        x = self.otoget_range()
        for i in range(1,x+1):
            for x in  self.otoget_divs(i):
                opis = x.find("h2").find("a")
                link = opis['href']
                try:
                    opis += x.find("h3").get_text()
                except:
                    pass
                opis = re.sub('\W+',' ', opis.get_text())
                cena = int(x.find("span", {"class":"offer-price__number ds-price-number"}).find("span").get_text().split(",")[0].replace(" ",""))
                adres = x.find("span",{"class":"ds-location-city"}).get_text()
                q=f'SELECT adres, cena, link, opis FROM moto WHERE adres="{adres}" AND cena="{cena}" AND opis="{opis}"'
                ins = self.db.execute(q)
                if not ins.fetchall():
                    self.db.execute("INSERT INTO moto (link, opis, cena, adres, diw) VALUES (?,?,?,?,?)",(link, opis, cena, adres, str(x)))
                    q=f'SELECT cena, link FROM moto WHERE adres="{adres}" AND opis="{opis}" AND cena!="{cena}"'
                    ins = self.db.execute(q)
                    repeated = ins.fetchall()
                    if repeated:
                        p = ""
                        for i in repeated:
                            p+=f'<a href="{i[1]}">Link</a> <h3 align="right">{i[0]}</h3><br />'
                        Skrap.diwy.append((x, int(cena), p))
                    else:
                        Skrap.diwy.append((x, int(cena)))
                #else:
                #    Skrap.diwy.append((x, int(cena)))
    def create_website(self, s):
        Skrap.diwy.sort(key=lambda x: x[1])
        fil = "/home/mateusz/"+self.baza.split(".")[0]+"olxall.html"
        print("Create file at ", time.strftime('Dzień %d-%m %H:%M:%S', time.localtime(time.time())))
        with open(fil, "w") as f:
            f.write(time.strftime('Dzień %d-%m %H:%M:%S', time.localtime(time.time())))
            f.write("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------<br>")
            for x, i in enumerate(Skrap.diwy):
                f.write(f'<p>{x}</p>')
                f.write(str(i[0]))
                try:
                    f.write(str(i[2]))
                except:
                    pass
#        os.system(f'xdg-open {fil}')
        if s==0:
            self.sql.close()
        else:
            self.set_markers()
    def web_base(self):
        #q='CREATE TABLE moto_stare AS SELECT * FROM moto'
        #q='DROP TABLE moto_stare'
        #Opel Omega 3
        #self.db.execute(q)
        #q='SELECT * FROM sqlite_master'
        q='SELECT diw FROM moto ORDER BY cena'
        #q='DELETE FROM moto WHERE opis LIKE "Opel%" AND adres="Biała Podlaska"'
        #self.db.execute(q)
        ins = self.db.execute(q)
        #for i in ins:
            #print(i)
        with open("file.html", "w") as f:
            for x, i in enumerate(ins):
                f.write(f'<p>{x}</p>')
                f.write(i[0])
        os.system('xdg-open file.html')
        #self.sql.commit()
        self.sql.close()

x = Skrap("https://www.olx.pl/motoryzacja/motocykle-skutery/radzyn-podlaski/?search%5Bfilter_float_price%3Ato%5D=10000&search%5Bfilter_float_year%3Afrom%5D=2004&search%5Bfilter_float_enginesize%3Afrom%5D=550&search%5Border%5D=filter_float_price%3Aasc&search%5Bdist%5D=300")
Skrap("https://www.otomoto.pl/motocykle-i-quady/od-2004/radzyn-podlaski/?search%5Bfilter_float_price%3Ato%5D=10000&search%5Bfilter_float_engine_capacity%3Afrom%5D=555&search%5Border%5D=created_at%3Adesc&search%5Bdist%5D=300&search%5Bcountry%5D=")
#x = Skrap()
#x = Skrap()
x.create_website(0)
#x.web_base()
#x = Skrap()
#x.web_base()
#x.set_address()
#x.set_markers()
