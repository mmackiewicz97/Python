import requests
import time

def pobierz_warunki_meteo():
    teraz = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    url = 'http://warszawa.infometeo.pl/'
    strona = requests.get(url).text
    czesc1 = strona.split('<pre class="metar"')
    czesc2 = czesc1[1].split("</pre>")

    with open("meteo.txt", "a") as plik:
        plik.write(teraz+"\n" + czesc2[0] + "\n***********************************\n")
    print("Pobrano dane meteo", teraz)
pobierz_warunki_meteo()
#for i in range(3):
#    time.sleep(2)
#    pobierz_warunki_meteo()
# while True:
#     time.sleep(3600)
#     pobierz_warunki_meteo()
