from tkinter import *
from PIL import ImageTk, Image
window = Tk()
window.attributes('-zoomed', True)
window.title('Zdjęciowybieracz')

photoMaxSizeWidth=1400
photoMaxSizeHeight=670
frame = Frame(window)
frame.pack()
button = Button(frame, text='Poprzednie', width=10, command=window.destroy)
button.pack(side=LEFT)
button = Button(frame, text='Wybierz', width=10, command=window.destroy)
button.pack(side=LEFT)
button = Button(frame, text='Następne', width=10, command=window.destroy)
button.pack(side=LEFT)

canvas = Canvas(window, width=photoMaxSizeWidth, height=photoMaxSizeHeight)
canvas.pack()

def load_img(photo):
    im = Image.open(photo)
    W=im.width
    H=im.height
    if W>H:
        NewW = photoMaxSizeWidth
        NewH = int(photoMaxSizeWidth*H/W)
    else:
        NewH = photoMaxSizeHeight
        NewW = int(photoMaxSizeHeight*W/H)
    im=im.resize((NewW, NewH))
    return im
img = ImageTk.PhotoImage(load_img('xd.jpg'))
canvas.create_image(650, 0, image=img, anchor=N)
window.mainloop()
