from tkinter import *
import os
from PIL import ImageTk, Image
from tkinter.filedialog import askdirectory

class Galery:
    def __init__(self):
        self.window = Tk()
        self.window.attributes('-zoomed', True)
        self.window.title('Zdjęciowybieracz')
        menubar = Menu(self.window)
        self.window.config(menu=menubar)

        filemenu=Menu(menubar)
        menubar.add_cascade(label='Plik', menu=filemenu)
        menubar.add_command(label='Pomoc', command=self.get_help)
        filemenu.add_command(label='Otwórz', command=self.get_path)
        filemenu.add_command(label='Zamknij', command=self.window.quit)

        frame = Frame(self.window)
        frame.pack()
        button = Button(frame, text='Poprzednie', width=10, command=lambda: self.move(-1))
        button.pack(side=LEFT)
        button = Button(frame, text='Wybierz', width=10, command=self.wybierz)
        button.pack(side=LEFT)
        button = Button(frame, text='Następne', width=10, command=lambda: self.move(+1))
        button.pack(side=LEFT)

        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        self.photoMaxSizeWidth=int(0.9*w)
        self.photoMaxSizeHeight=int(0.8*h)
        self.current = 0

        self.canvas = Canvas(self.window, width=self.photoMaxSizeWidth, height=self.photoMaxSizeHeight)
        self.canvas.pack()
        self.window.mainloop()

    def get_path(self):
        self.path = askdirectory()
        self.get_photos()
        self.move(1)

    def get_help(self):
        top = Toplevel()
        top.title("Pomoc")
        l = Label(top, text="1. Z menu kliknij plik\n2. Kliknij otwórz\n3. Wybierz folder ze zdjęciami\n4.Wybierz najładniejsze zdjęcia, zostaną przeniesione do pliku 'Wybrane' w tym samym folderze", font=('Times', '14'))
        l.pack()
        b = Button(top, text="Zamknij to okno", command=top.destroy)
        b.pack()

    def get_photos(self):
        self.photos = []
        for photo in os.listdir(self.path):
            if photo.endswith(".jpg") or photo.endswith(".jpeg") or photo.endswith(".png"):
                self.photos.append(os.path.join(self.path, photo))

    def load(self,photo):
        im = Image.open(photo)
        W=im.width
        H=im.height
        if W>H:
            NewW = self.photoMaxSizeWidth
            NewH = int(self.photoMaxSizeWidth*H/W)
            if NewH > self.photoMaxSizeHeight:
                NewH = self.photoMaxSizeHeight
                NewW = int(self.photoMaxSizeHeight*W/H)
        else:
            NewH = self.photoMaxSizeHeight
            NewW = int(self.photoMaxSizeHeight*W/H)
            if NewW>self.photoMaxSizeWidth:
                NewW = self.photoMaxSizeWidth
                NewH = int(self.photoMaxSizeWidth*H/W)
        im=im.resize((NewW, NewH))
        return ImageTk.PhotoImage(im)

    def move(self,delta):
        self.current += delta
        try:
            if len(self.photos)>0:
                if self.current >= len(self.photos):
                    self.current = 0
                elif self.current < 0:
                    self.current = len(self.photos)-1
                photo = self.photos[self.current]
                img = self.load(photo)
                self.canvas.create_image(self.photoMaxSizeWidth/2, 0, image=img, anchor=N, tags='photo')
                self.canvas.image=img
        except AttributeError:
            self.canvas.create_text(self.photoMaxSizeWidth/2,220,font="Times 20 italic bold",text="Wybierz folder ze zdjęciami", tags='wyb')


    def wybierz(self):
        try:
            if len(self.photos)>0:
                photo = self.photos.pop(self.current)
                try:
                    os.makedirs(self.path+"/Wybrane")
                except FileExistsError:
                    pass
                os.rename(photo, self.path+"/Wybrane/"+photo.split("/")[-1])
                self.move(1)
            else:
                self.canvas.delete('photo')
                self.canvas.delete('wyb')
                self.canvas.create_text(self.photoMaxSizeWidth/2,220,font="Times 20 italic bold",text="To już wszystkie zdjęcia ;)")
        except AttributeError:
            self.canvas.create_text(self.photoMaxSizeWidth/2,220,font="Times 20 italic bold",text="Wybierz folder ze zdjęciami", tags='wyb')

Galery()
