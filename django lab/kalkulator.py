import tkinter as tk
from tkinter import StringVar
from tkinter import font
root = tk.Tk()
default_font = font.nametofont("TkDefaultFont")
default_font.configure(size = 14)
root.option_add("*Font", default_font)
root.geometry("450x210")
root.title("Kalkulator pro wersja")
root.resizable(False,False)

wynik = StringVar()
dzialanie  = ""

e = tk.Entry(root, textvariable = wynik, width = 30)
e.grid(columnspan = 4)

def wcisnij(num):
    global dzialanie
    dzialanie += str(num)
    if var2.get() == 0:
        try:
            wynik.set(bin(int(dzialanie))[2:])
        except:
            wynik.set(dzialanie)
    else:
        wynik.set(dzialanie)

def czysc():
    global dzialanie
    dzialanie = ""
    wynik.set("")

def oblicz():
    try:
        global dzialanie
        wynik_koncowy = str(eval(dzialanie))
        if var2.get() == 0:
            wynik_koncowy = float(wynik_koncowy)
            wynik_koncowy = bin(int(wynik_koncowy))[2:]
        wynik.set(wynik_koncowy)
    except Exception as e:
        print(e)
        wynik.set("Blad!")
        dzialanie = ""

var2 = tk.IntVar()
t1 = tk.Radiobutton(root, text = "sys 10", variable = var2, value = 1, command = lambda: wcisnij(""))
t1.select()
t1.grid(row = 1, column = 1)
t2 = tk.Radiobutton(root, text = "sys 2", variable = var2, value = 0, command = lambda: wcisnij("")).grid(row = 1, column = 2)

tk.Button(root, text = "1", command = lambda: wcisnij(1), width = 7).grid(row = 2, column = 0)
tk.Button(root, text = "2", command = lambda: wcisnij(2), width = 7).grid(row = 2, column = 1)
tk.Button(root, text = "3", command = lambda: wcisnij(3), width = 7).grid(row = 2, column = 2)
tk.Button(root, text = "4", command = lambda: wcisnij(4), width = 7).grid(row = 3, column = 0)
tk.Button(root, text = "5", command = lambda: wcisnij(5), width = 7).grid(row = 3, column = 1)
tk.Button(root, text = "6", command = lambda: wcisnij(6), width = 7).grid(row = 3, column = 2)
tk.Button(root, text = "7", command = lambda: wcisnij(7), width = 7).grid(row = 4, column = 0)
tk.Button(root, text = "8", command = lambda: wcisnij(8), width = 7).grid(row = 4, column = 1)
tk.Button(root, text = "9", command = lambda: wcisnij(9), width = 7).grid(row = 4, column = 2)
tk.Button(root, text = "0", command = lambda: wcisnij(0), width = 7).grid(row = 5, column = 0)
tk.Button(root, text = "+", command = lambda: wcisnij("+"), width = 7, bg = "SpringGreen3").grid(row = 2, column = 3)
tk.Button(root, text = "-", command = lambda: wcisnij("-"), width = 7, bg = "SpringGreen3").grid(row = 3, column = 3)
tk.Button(root, text = "*", command = lambda: wcisnij("*"), width = 7, bg = "SpringGreen3").grid(row = 4, column = 3)
tk.Button(root, text = "/", command = lambda: wcisnij("/"), width = 7, bg = "SpringGreen3").grid(row = 5, column = 3)
tk.Button(root, text = "=", command = oblicz, width = 7, bg = "tomato").grid(row = 5, column = 2)
tk.Button(root, text = "C", command = czysc, width = 7, bg = "aquamarine").grid(row = 5, column = 1)

root.mainloop()
