from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, datetime
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
#for child in bsObj.find("table",{"id":"giftList"}).children:
    #print(child)
#for child in bsObj.find("table",{"id":"giftList"}).descendants:
    #print(child)
#for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
#    print(sibling)
#print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
#for image in images:
#    print(image["src"])
html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html)
#for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
#    if 'href' in link.attrs:
#        print(link.attrs['href'])

#random.seed(datetime.datetime.now())
pages = set()
def getLinks(articleUrl):
#    html = urlopen("http://en.wikipedia.org"+articleUrl)
#    bsObj = BeautifulSoup(html)
#    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
#We have encountered a new page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
#links = getLinks("/wiki/Kevin_Bacon")
#while len(links) > 0:
#    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
#    print(newArticle)
#    links = getLinks(newArticle)
