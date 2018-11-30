from re import sub
import re
def printer_error(s):   #s = "aaammxxxaam" if not a-m == error result sum [a-m]/all
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

def printer_error2(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))

def bin(arr):       #arr = [1, 0, 0, 1] to decimal
    return int("".join(map(str, arr)), 2)

def tribonacci(signature, n): #kolejny element to suma 3 wcześniejszych
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res

def to_camel_case(text):  #text [a-in-middle_of] result aInMiddleOf
    b=[]
    a=text.replace("-", " ").replace("_", " ").split(" ")
    for i in a:
        if i=="a" or i=="the" or i=="an":
            b.append(i)
        else:
            if i!="":
                x = str(i[0].upper()+i[1:])
                b.append(x)

def too_camel_case(s): #s=the-Cos_tam   = theCosTam
    return s[0] + s.title().translate(None, "-_")[1:] if s else s

def cezar(x):
    intab = "abcde"
    outtab = "bcdef"
    trantab = str.maketrans(intab, outtab)
    print(x.translate(trantab)) #change abc to bcd

def high(x): #wyraz najwyżej punktowany w alfabecie np abc = 1+2+3 xyz=24+25+26
    d = {}
    z=1
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        d[i]=z
        z+=1
    sum = []
    a = x.split(" ")
    for i in a:
        licznik = 0
        for j in i:
            licznik = licznik + d.get(j)
        sum.append(licznik)
    return a[sum.index(max(sum))]
    #return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

def array_diff(a, b): #a=[1,1,2,3] b=[1,1,1,2] =[3]
    for i in b:
        while True:
            try:
                a.remove(i)
                break
            except:
                break
    return a
    #return [x for x in a if x not in b]

def validBraces(string): #string = "{[[}]]" sprawdzenie czy nawiasy się dobrze zamykają
    for i in string:
        string = string.replace("()", "").replace("{}", "").replace("[]", "")
    if string == "":
        print("True")
    else:
        print("False")

def duplicate_count(s): #s="aabcdd" return 2 powtórzenia w stringu (a 2x oraz d 2x)
    return len([c for c in set(s.lower()) if s.lower().count(c)>1])

def getCount(inputStr): #return number of vowels
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

def dig_pow(n, p): #4^3+6^4+2^5.../46288 = 51
    elem = []
    for i in str(n):
        elem.append(int(i)**p)
        p+=1
    if sum(elem)%n==0:
        print(sum(elem)/n)
    else:
        print(-1)
def dig_pow2(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  print(s/n if s%n==0 else -1)
def song_decoder(song): #song = "WUBEJWUBBEWUBCEWUBDE" --> EJ BE CE DE
    return " ".join(song.replace('WUB', ' ').split())
def DNA_strand(dna):
    pairs = {'A':'T','T':'A','C':'G','G':'C'}
    return ''.join([pairs[x] for x in dna])
    #return dna.translate(string.maketrans("ATCG","TAGC"))
def digital_root(n):  #n = 123 1+2+3=6
    return n if n < 10 else digital_root(sum(map(int,str(n))))
def digital_root2(n):
  return n%9 or n and 9
def count_smileys(arr):
    pair = {":":("-)","~)",")","-D","~D","D"),";":(")","~)","-)","D","~D","-D")}
    z=0
    for i in arr:
        if i[0] in pair:
           for k in pair[i[0]]:
               if i[1:] ==k:
                  z+=1
    print(z)
from re import findall
def count_smileys(arr): #count_smileys([":)", ";(", ";~D"])
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))
def order(sen): #order("Tgi1s t3st is2:")
    t=[]
    for i in sen.split():
        for k in i:
            try:
                if int(k):
                    t.append((i,k))
            except:
                pass
    def takesec(elem):
        return elem[1]
    t.sort(key=takesec)
    r=[]
    for i in t:
        r.append(i[0])
    if sen=="":
        print( "")
    else:
        print( ' '.join(r))
def order2(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

from ipaddress import IPv4Address
def numberAndIPaddress(s):
    return str(int(IPv4Address(s))) if '.' in s else str(IPv4Address(int(s)))
def Int2IP(ipnum):
    o1 = int(ipnum / 16777216) % 256
    o2 = int(ipnum / 65536) % 256
    o3 = int(ipnum / 256) % 256
    o4 = int(ipnum) % 256
    return '%(o1)s.%(o2)s.%(o3)s.%(o4)s' % locals()
def IP2Int(ip):
    o = map(int, ip.split('.'))
    return str((16777216 * o[0]) + (65536 * o[1]) + (256 * o[2]) + o[3])
def unique_in_order(iterable):
    a = []
    a.append(iterable[0])
    for i in range(len(iterable)):
        try:
            if iterable[i] != iterable[i+1]:
                a.append(iterable[i+1])
        except:
            pass
def tower_builder(n):
    for i in [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]:
        print(i)
