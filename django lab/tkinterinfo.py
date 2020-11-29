import tkinter as tk
from tkinter import font
from tkinter import messagebox

x = 0

def labelConfig(label, txt):
    label.config(text=txt, fg = "light green", bg = "dark green")
def show_entry_fields():
    messagebox.showinfo("Message", e1.get())
def add(ent, y):
    global x
    x += y
    ent.delete(0, "end")
    ent.insert(tk.END, str(x))
def msg(var):
    print(var.get())
def valPrnt():
    print(varR.get())

root = tk.Tk()
default_font = font.nametofont("TkDefaultFont")
default_font.configure(size = 24)
root.option_add("*Font", default_font)
tk.Label(root, text="Write something").grid(row=0, column = 0)

var1 = tk.BooleanVar()
tk.Checkbutton(root, text = "opcja 1", variable = var1, command = lambda: msg(var1)).grid(row = 1, column = 0)
var2 = tk.BooleanVar()
tk.Checkbutton(root, text = "opcja 2", variable = var2, command = lambda: msg(var2)).grid(row = 1, column = 1)

varR = tk.IntVar()
tk.Radiobutton(root, text = "opcja 3", variable = varR, command = valPrnt, value = 1).grid(row = 4)
tk.Radiobutton(root, text = "opcja 4", variable = varR, command = valPrnt, value = 2).grid(row = 4, column = 2)

e1 = tk.Entry(root)
e1.grid(row = 0, column = 1)
#sticky przyciąganie w ramach komórki w danym kierunku
#pady = padding
tk.Button(root, text = "Quit", command = root.quit).grid(row = 1, column = 2, sticky = tk.W, pady = 4)
tk.Button(root, text = "Show", command = show_entry_fields).grid(row = 1, column = 3)
tk.Button(root, text = "1", command = lambda: add(e1, 1)).grid(row = 2, column = 0)
tk.Button(root, text = "2", command = lambda: add(e1, 2)).grid(row = 2, column = 3)
# l1 = tk.Label(root, text = "L1", bg = "green")
# l2 = tk.Label(root, text = "L2", bg = "red")
# l3 = tk.Label(root, text = "L3", bg = "blue")
# #l1.pack()
# l1.grid(row = 0, column = 0, columnspan = 2)
# #rowspan dla wierszy
# l2.grid(row = 1, column = 0)
# l3.grid(row = 1, column = 1)
# #labelConfig(l1, "123")

#fill - rozciąga się tk.Y
#side tk.LEFT
# do pack()
root.mainloop()