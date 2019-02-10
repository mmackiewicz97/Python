import imapclient
import imaplib
import re
import datetime
from selenium import webdriver
imaplib._MAXLINE=10000000 #zwiększenie rozmiaru pobieranych wiadomości
imapObj = imapclient.IMAPClient('poczta.interia.pl',ssl=True) #imap dla danej poczty
imapObj.login('nazwauzytkownika','haslo')
#for i in imapObj.list_folders():
#    print(i[2])
imapObj.select_folder('INBOX', readonly=True)
#UIDs = imapObj.search([u'ALL'])
UIDs = imapObj.search([u'SINCE', datetime.date(2017,1,1)])
rawMessages=imapObj.fetch(UIDs,['BODY[]', 'FLAGS'])
pattern=r"List-Unsubscribe: <(http://[^>]+)>"
regex=re.compile(pattern)
f = open("unsuby.txt", "w")
f.write("Ilosc wiadomosci: {}".format(len(UIDs)))
f.write("\n \n")
for i in UIDs:
    x = regex.findall(str(rawMessages[i][b'BODY[]']))
    try:
        f.write(str(x[0])+"\n")
    except:
        pass
f.close()
browser=webdriver.Firefox()
with open("unsuby.txt", 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        link = lines.pop()
        browser.get(link)
        time.sleep(2)
        try:
            button=browser.find_element_by_tag_name('button').click()
        except:
            pass
        try:
            button=browser.find_element_by_tag_name('btn').click()
        except:
            pass
        time.sleep(1)
#import pyzmail #do szczegółow danej wiadomości
#message=pyzmail.PyzMessage.factory(rawMessages[16771][b'BODY[]'])
#print(message.get_subject())
#print(message.get_addresses('from'))
#print(message.get_addresses('to'))
#print(message.get_addresses('cc'))
#print(message.get_addresses('bcc'))
#print(message.text_part != None)
#print(message.text_part.get_payload().decode(message.text_part.charset))
#print(message.html_part != None)
#print(message.html_part.get_payload().decode(message.html_part.charset))
imapObj.logout()
