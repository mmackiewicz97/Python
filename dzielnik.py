'''Program wczytuje liczbe n, nastepnie tyle liczb z zakresu 1-25 000 000
wyswietla ile mozna stworzyc par (a,b) takich ze
b jest dzielnikiem a'''
liczba_elementow = [0 for i in range(0, 25000001)]
wynik = 0
minimum = 25000001
maximum = 0

n = int(input())
i = n
while i:
	i += 1
	liczba = int(input())
	liczba_elementow[liczba] += 1
	if(minimum > liczba):
		minimum = liczba
	if(maximum < liczba):
		maximum = liczba

i = minimum
while i <= maximum:
	if(liczba_elementow[i] > 0):
		wynik += liczba_elementow[i]**2 - liczba_elementow[i]
		j = i*2
		while j <= maximum:
			wynik += liczba_elementow[i] * liczba_elementow[j]
			j += 1
	i += 1
print(wynik)
