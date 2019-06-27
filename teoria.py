#Shift+F6 zmiana nazwy zmiennej wszędzie gdzie występuje
#Ctrl + / hashowanie zaznaczonych linijek
# To find the maximum or minimum of some numbers or a list, you can use max or min.
# To find the distance of a number from zero (its absolute value), use abs.
# To round a number to a certain number of decimal places, use round.
# To find the total of a list, use sum.

from collections import OrderedDict
d1 = dict() #słownik
d1["a"]=1
d1['b']=1
d3 = {"a": 1, "b": 2}
d4 = OrderedDict([("a", 1), ("b", 2)])
d2=OrderedDict()
d2['a']=1
d2['b']=1

nums = [55, 44, 33, 22, 11]
#for m, i in enumerate(nums):
    #print(m, i)
#print(dir())    #wyświetla istniejące zmienne
#print(locals())
#\n nowa linia
#\t tabulator

#if all([i > 5 for i in nums]):
   #print("All larger than 5")

#if any([i % 2 == 0 for i in nums]):
   #print("At least one is even")

#for v in enumerate(nums):
   #print(v)
# try:
# except ZeroDivisionError:    pass nic nie rób
# finally:
# ImportError: an import fails;
# IndexError: a list is indexed with an out-of-range number;
# NameError: an unknown variable is used;
# SyntaxError: the code can't be parsed properly;
# TypeError: a function is called on a value of an inappropriate type;
# ValueError: a function is called on a value of the correct type, but with an inappropriate value.
# temp = -10
# assert (temp >= 0), "Colder than absolute zero!"
# Sending "r" means open in read mode, which is the default.
# Sending "w" means write mode, for rewriting the contents of a file.
# Sending "a" means append mode, for adding new content to the end of the file.
# Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).
# myfile = open("filename.txt", "r")
# print(myfile.read(16)) 16 bajtów
#             .readlines()
# for line in file:
#     print(line)
# myfile.close()
# file = open("new.txt", "w")
# file.write("This has been written to a file")
# file.close()
# file = open("new.txt", "r")
# #print(file.read())
# file.close()
# with open("filename.txt") as f:   zamyka plik nawet jak są błędy
#    print(f.read())
# x=1245/4
#print(type(x))
#print(round(x, 3)) #zaokrąglanie
#print(round(3.1+0.5)) #do pełnych w górę - w dół
# y="3"
# print(int(y)+2)
# print("%3.f" %x)
# słownik = {"ja" : [1, 2, 3],"ty" : [1, 2, 5]}
# print(słownik.get("on", "w zamian Ty"))
# tablica = []
# tablica1 = ["tekst", 1, 2]
# tablica.append("tekst2")
# tablica.extend(tablica1)
# tablica.append(tablica1)
# print(tablica[4]) #[4][2]
# print(tablica1[::-1])
# tablica.insert(2, "x") #wstawia na 2 miejscu x
# tablica.remove("tekst")
# tablica.index(2,0,6)  #którą pozycję ma 2 w tablicy od 1 do 7 elementu
# print(tablica1.pop(1))
# print(tablica1.count("a"))
# tablica1.copy()
# tablica2 = [1,3,5]
# tablica2.sort()
# tablica1.reverse()
# tablica.clear()
# print(tablica2)
# print("witaj {} {} ;)" .format(*tablica2))
# print("witaj %d %d" %(tablica2[0], tablica2[1])) #%s string %d int %f float %.3f długość rozszerzenia
# print("coś tam %d" %len(tablica2))
# print("witaj {} " .format(tablica2))
text = "jakiśtekst z jakimiś literami tak żeby się powtarzały"
def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count
for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  #print("{0} - {1}%".format(char, round(perc, 2)))
# kombinacja = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(kombinacja)
# list = [["jan", "wiek= ", 15],["janina", "wiek= ", 20],["janek", "wiek= ", 10]]
# list.sort(key= lambda x: x[2])
# print(list)
#
# hex = 156
# print("hex w 16: %x" %hex)
# hex2 = 15**2 #potęga % reszta z dzielenia
#
# name = "Janeczek jest sPOkO"
# print(name.upper())
# print(name.startswith("Janeczek"))
# print(name.lower().endswith("spoko"))
# name.split(' ') #dzieli string na tablice w miejscu spacji
# name.join() działa odwrotnie do split
# join - joins a list of strings with another string as a separator.
# replace - replaces one substring in a string with another.
# print(name)
# != różne od == równe = ma wartość
#pyplot color
#character      color
# ‘b’   blue
#‘g’    green
#‘r’    red
#‘c’    cyan
#‘m’    magenta
#‘y’    yellow
#‘k’    black
#‘w’    white

#Alfabet
# for i in range(65, 91):
#     print(chr(i))

def add_five(x):
  return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))  #The function map takes a function and an iterable as arguments,
#print(result)                       # and returns a new iterable with the function applied to each argument.
result2 = list(map(lambda x: x+5, nums))
res = list(filter(lambda x: x%2==0, nums)) #The function filter filters an iterable by removing items that
#print(res)                                 # don't match a predicate (a function that returns a Boolean).

def countdown():
  i=5
  while i > 0:
    yield i
    i -= 1
#for i in countdown():
    print(i)
def decor(func):
    def wrap():
        print("=====")
        func()
        print("=====")
    return wrap
@decor
def print_text():
  print("Hello world!")
#print_text()

nums = {1, 2, 1, 3, 1, 4, 5, 6} #set() Basic uses of sets include membership testing and the elimination of duplicate entries.
# print(nums)
nums.add(-7)
nums.remove(3)
# print(nums)
# print(3 not in nums)
# The union operator | combines two sets to form a new one containing items in either.
# The intersection operator & gets items only in both.
# The difference operator - gets items in the first set but not in the second.
# The symmetric difference operator ^ gets items in either set, but not both.
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

# print(first | second)
# print(first & second)
print(first - second)
print(second - first)
#print(first ^ second)

# When to use a dictionary:
# - When you need a logical association between a key:value pair.
# - When you need fast lookup for your data, based on a custom key.
# - When your data is being constantly modified. Remember, dictionaries are mutable.
#
# When to use the other types:
# - Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
# - Use a set if you need uniqueness for the elements.
# - Use tuples when your data cannot change.

# The module itertools is a standard library that contains several functions that are useful in functional programming.
# One type of function it produces is infinite iterators.
# The function count counts up infinitely from a value.
# The function cycle infinitely iterates through an iterable (for instance a list or string).
# The function repeat repeats an object, either infinitely or a specific number of times.
# takewhile - takes items from an iterable while a predicate function remains true;
# chain - combines several iterables into one long one;
# accumulate - returns a running total of values in an iterable.
# product and permutation.
# These are used when you want to accomplish a task with all possible combinations of some items.
import itertools
for i in itertools.count(3):
  #print(i)
  if i >=11:
    break
nums = list(itertools.accumulate(range(8)))
#print(nums)
#print(list(itertools.takewhile(lambda x: x<= 6, nums)))
letters = ("A", "B", "C")
#print(list(itertools.product(letters, range(2))))
#print(list(itertools.permutations(letters)))
a = {1,2}
#print(list(itertools.product(range(3),a)))
class A:
    def spam(self):
        print(1)
    def __init__(self, x ,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return A(self.x + other.x, self.y + other.y)
class B(A):
    def spam(self):
        print(2)
        super().spam() #pobieranie od super klasy funkcji pierwotnej
#B(2,3).spam()
a1 = A(1,2)
a2 = A(3,4)
a= a1+a2
#print(a.x)
# More magic methods for common operators:
# __add__ for +
# The expression x + y is translated into x.__add__(y).
# __sub__ for -
# __mul__ for *
# __truediv__ for /
# __floordiv__ for //
# __mod__ for %
# __pow__ for **
# __and__ for &
# __xor__ for ^
# __or__ for |
# A().__rxor__(B())
# The expression x + y is translated into x.__add__(y).
# However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called.
# __lt__ for <
# __le__ for <=
# __eq__ for ==
# __ne__ for !=
# __gt__ for >
# __ge__ for >=
#
# If __ne__ is not implemented, it returns the opposite of __eq__.
# __len__ for len()
# __getitem__ for indexing
# __setitem__ for assigning to indexed values
# __delitem__ for deleting indexed values
# __iter__ for iteration over objects (e.g., in for loops)
# __contains__ for in
# __del__ for delete object
# he __repr__ magic method is used for string representation of the instance.
class SpecialString:
  __hiddenhiddencont = "coś"
  def __init__(self, cont):
    self.cont = cont
    self._hiddencont = 2*cont
  def print_hidden(self):
      print(self.__hiddenhiddencont)
  def __gt__(self, other):
    for index in range(len(other.cont)+1):
      result = other.cont[:index] + ">" + self.cont
      result += ">" + other.cont[index:]
      print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs")
#spam > eggs
# class Spam:
#   __egg = 7
#   def print_egg(self):
#     print(self.__egg)
#
# s = Spam()
# try:
#     s.print_egg() #też działa
#     print(s._Spam__egg) #prywatna metoda
#     print(s.__egg)
# except AttributeError:
#     print("zrob cos po wyskoczeniu błędu")


# Methods of objects we've looked at so far are called by an instance of a class, which is then passed to the self parameter of the method.
# Class methods are different - they are called by a class, which is passed to the cls parameter of the method.
# A common use of these are factory methods, which instantiate an instance of a class, using different parameters than those usually passed to the class constructor.
# Class methods are marked with a classmethod decorator.
# new_square is a class method and is called on the class, rather than on an instance of the class. It returns a new object of the class cls.
# Technically, the parameters self and cls are just conventions; they could be changed to anything else. However, they are universally followed, so it is wise to stick to using them.
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def calculate_area(self):
    return self.width * self.height

  @classmethod
  def new_square(cls, side_length):
    return cls(side_length, side_length)

square = Rectangle.new_square(5)
#print(square.calculate_area())

# Static methods are similar to class methods, except they don't receive any additional arguments; they are identical to normal functions that belong to a class.
# They are marked with the staticmethod decorator.
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True
    @property
    def pineapple_allowed(self):
        return False

pizza = Pizza(["cheese", "tomato"])
#print(pizza.pineapple_allowed)
#pizza.pineapple_allowed = True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
  pizza = Pizza(ingredients)
#Static methods behave like plain functions, except for the fact that you can call them from an instance of the class.
#
# Properties provide a way of customizing access to instance attributes.
# They are created by putting the property decorator above a method, which means when the instance attribute with the same name as the method is accessed, the method will be called instead.
# One common use of a property is to make an attribute read-only.

# Properties can also be set by defining setter/getter functions.
# The setter function sets the corresponding property's value.
# The getter gets the value.
# To define a setter, you need to use a decorator of the same name as the property, followed by a dot and the setter keyword.
# The same applies to defining getter functions.
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    self._pineapple_allowed = False

  @property
  def pineapple_allowed(self):
    return self._pineapple_allowed

  @pineapple_allowed.setter
  def pineapple_allowed(self, value):
    if value:
      password = input("Enter the password: ")
      if password == "Al":
        self._pineapple_allowed = value
      else:
        raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
#print(pizza.pineapple_allowed)
#pizza.pineapple_allowed = True
#print(pizza.pineapple_allowed)

#Regular expressions
# The function re.search finds a match of a pattern anywhere in the string.
# The function re.findall returns a list of all substrings that match a pattern.
# The function re.finditer does the same thing as re.findall, except it returns an iterator, rather than a list.
# import re
#
# pattern = r"spam"
#
# if re.match(pattern, "eggspamsausagespam"):
#     print("Match")
# else:
#     print("No match")
#
# if re.search(pattern, "eggspamsausagespam"):
#     print("Match")
# else:
#     print("No match")
#
# print(re.findall(pattern, "eggspamsausagespam"))
# No match
# Match
# ['spam', 'spam']
#
# The regex search returns an object with several methods that give details about it.
# These methods include group which returns the string matched, start and end which return the start and ending positions of the first match, and span which returns the start and end positions of the first match as a tuple.
# pattern = r"pam"
#
# match = re.search(pattern, "eggspamsausage")
# if match:
#    print(match.group()) #pam
#    print(match.start()) #4
#    print(match.end())   #7
#    print(match.span())  #(4,7)
# re.sub(pattern, repl, string, max=0)
#
# This method replaces all occurrences of the pattern in string with repl, substituting all occurrences, unless max provided. This method returns the modified string.
# str = "My name is David. Hi David."
# pattern = r"David"
# newstr = re.sub(pattern, "Amy", str)

#Metacharacters
#. zastępuje jeden znak
#^ and $, start and end of string
#pattern = r"[aeiou]" matches all strings that contain any one of the characters defined. [A-Za-z][0-9]  ^[1-5] bez 1-5
#The metacharacter * means "zero or more repetitions of the previous thing".
#+ -one or more repetitions
#pattern = r"g+"   r"[a^]*"
#The metacharacter ? means "zero or one repetitions".
#pattern = r"ice(-)?cream"

#(spam) represents a group in the example pattern shown above

# Curly braces {} can be used to represent the number of repetitions between two numbers.
# The regex {x,y} means "between x and y repetitions of something".
# Hence {0,1} is the same thing as ?.
# If the first number is missing, it is taken to be zero. If the second number is missing, it is taken to be infinity.
# pattern = r"9{1,3}$"
# A call of group(0) or group() returns the whole match.
# A call of group(n), where n is greater than 0, returns the nth group from the left.
# The method groups() returns all groups up from 1.
# pattern = r"a(bc)(de)(f(g)h)i"
# Named groups have the format (?P<name>...), where name is the name of the group, and ... is the content. They behave exactly the same as normal groups, except they can be accessed by group(name) in addition to its number.
# Non-capturing groups have the format (?:...). They are not accessible by the group method, so they can be added to an existing regular expression without breaking the numbering.
#pattern = r"(?P<first>abc)(?:def)(ghi)"
#match.group("first")
# |   This means "or", so red|blue matches either "red" or "blue".
# One useful special sequence is a backslash and a number between 1 and 99, e.g., \1 or \17. This matches the expression of the group of that number.
# pattern = r"(.+) \1"
# Note, that "(.+) \1" is not the same as "(.+) (.+)", because \1 refers to the first group's subexpression, which is the matched expression itself, and not the regex pattern.
# special sequences are \d, \s, and \w.
# These match digits, whitespace, and word characters respectively.
# In ASCII mode they are equivalent to [0-9], [ \t\n\r\f\v], and [a-zA-Z0-9_].
# \D, \S, and  \W - mean the opposite
# The sequences \A and \Z match the beginning and end of a string, respectively.
# The sequence \b matches the empty string between \w and \W characters, or \w characters and the beginning or end of the string. Informally, it represents the boundary between words.
# The sequence \B matches the empty string anywhere else.
# pattern = r"\b(cat)\b"
#
# match = re.search(pattern, "The cat sat!")
# pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
# [\w\.-]+ matches one or more word character, dot or dash.
# str = "Please contact info@sololearn.com for assistance"
#
# match = re.search(pattern, str)
# if match:
#    print(match.group())
#help()
#dir()
#hasattr()
#id()
#type()
#repr()
#callable()
#issubclass()
#isinstance()
#__doc__
#__name__
#def print_msg(number):
#    print(number)
#    def printer():
#        nonlocal number
#        number+=2
#        print(number)
#    printer()
#    print(number)
#
#print_msg(9)
head, *body, tail, _ = range(5) # "Początek środek, który jest tablicą i koniec".split()

from pathlib import Path
root = Path('post_sub_folder')
#print(root) #post_sub_folder
path = root # 'happy_user'
# Make the path absolute
#print(path.resolve()) #/home/mateusz/pyton/post_sub_folder/happy_user/
user = "Jane Doe"
action = "buy"
log_message = f'User {user} has logged in and did an action {action}.'
a = lambda x:x**2
#print(a(2))
b = [1,2,3]
#print(list(map(a,b))) #iterates all the lists (or dictionaries etc.) and calls the lambda function for each of their element.
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
vowels = ['a', 'e', 'i', 'o', 'u']
#print(list(filter(lambda x: (x in vowels) , alphabets)))
#returns a final list containing items for which the lambda function evaluates to True.
from functools import reduce
#print(reduce((lambda x, y: x + y), [1,2,3,4]))
