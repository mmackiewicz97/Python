import shelve, sys
from time import *
db = shelve.open('baza_pyton')
db['l'] = [1,2,3,4]
db['s'] = "tekst"
db.close()
db = shelve.open('baza_pyton')
print(db['l'])
db.close()
