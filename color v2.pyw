import PIL
from tkinter import *
from tkinter.font import Font
from pyautogui import screenshot
import time
from gethex import *
from fontsetup import font
from rootsetup import rootsetup, alpha

def getcoor(event):
    global point, run, mg
    point = root.winfo_pointerxy()
    root.unbind('<Button-1>')
    root.attributes("-fullscreen", False); root.attributes('-alpha', 1.0)
    root.config(bg='#252525', cursor='arrow')
    run=False
    mg.destroy()
    getcolor()
    
def getcolor():
    global point, colorcode, color

    colorboxframe.place(x=78, y=148)
    getcolorbuttonframe.place(x=78, y=88)
    colorcodebox.place(x=80, y=150)
    getcolorbutton.place(x=80, y=90)

    Rboxframe.place(x=131, y=231)
    Gboxframe.place(x=131, y=281)
    Bboxframe.place(x=131, y=331)

    RLabel.place(x=103, y=230)
    RBox.place(x=133, y=233)
    GLabel.place(x=103, y=280)
    GBox.place(x=133, y=283)
    BLabel.place(x=103, y=330)
    BBox.place(x=133, y=333)


    rc.set(color[0])
    gc.set(color[1])
    bc.set(color[2])

def startgetcoor():
    global colorcode, run, mg, color
    
    colorcodebox.place_forget()
    getcolorbutton.place_forget()
    colorboxframe.place_forget()
    getcolorbuttonframe.place_forget()

    Rboxframe.place_forget()
    Gboxframe.place_forget()
    Bboxframe.place_forget()
    
    RLabel.place_forget()
    GLabel.place_forget()
    BLabel.place_forget()

    RBox.place_forget()
    GBox.place_forget()
    BBox.place_forget()

    root.attributes('-alpha', 0.00)

    ss = screenshot()
    ss.save("s.png")
    
    root.attributes("-fullscreen", True)
    root.config(bg='white')
    root.attributes('-alpha', 0.01)
    root.bind('<Button-1>', getcoor)
    root.update()


    mg = Toplevel()
    mg.geometry('204x250')
    canvas = Canvas(mg, width=200, height=200, bg='black')
    canvas.grid(row=0, column=0, columnspan=2)
    gif1 = PhotoImage(file='s.png')
    gif1 = gif1.zoom(8,8)
    im = PIL.Image.open('s.png')
    rgb_im = im.convert('RGB')
    rrrcolor = StringVar()
    showfont = font(20, 'BL')
    color = Label(mg, textvariable=rrrcolor, font=showfont)
    color.grid(row=1, column=0, columnspan=2)
    root.config(cursor='crosshair')

    run=True

    while run:
        point = mg.winfo_pointerxy()
        try:
            alpha(0.008, root)
            color = rgb_im.getpixel((point[0], point[1]))
            alpha(0.01, root)
            rrrcolor.set(gethexbyrgblist(color))
            canvas.delete("all")
            canvas.create_image(-point[0]*8+100-4, -point[1]*8+100-4, image=gif1, anchor=NW)
            canvas.create_rectangle(200/2-4, 200/2-4, 200/2+4, 200/2+4, outline="#f11", width=0.5)
            canvas.update()
            mg.update()
        except:
            point = mg.winfo_pointerxy()
            alpha(0.008, root)
            color = rgb_im.getpixel((1, 1))
            alpha(0.01, root)
            rrrcolor.set(gethexbyrgblist(color))
            root.update()

root = rootsetup('300x400', 'Color Picker', '#252525', False, False, 1)

def e_getcolor(event):
    getcolorbutton['bg'] = '#565656'
    getcolorbutton['fg'] = 'white'
def l_getcolor(event):
    getcolorbutton['bg'] = '#252525'
    getcolorbutton['fg'] = 'white'

buttonfont = font(15, 'BSB')
entryfont = font(20, 'BL')
labelfont = font(15, 'BSB')
rgbentryfont = font(15, 'BL')
titlefont = font(30, 'BSB')

getcolorbuttonframe = Frame(root, width=143, height=46, bg='#FFFFFF')
getcolorbutton = Button(root,text='PICK COLOR',command=startgetcoor,relief=FLAT,font=buttonfont,bg='#252525',fg='white',activebackground='#565656',activeforeground='white',width=11,padx=5)

colcode = StringVar()

title = Label(root, text='COLOR PICKER',font=titlefont, bg='#252525', fg='white')
title.place(x=10, y=10)

colorboxframe = Frame(root, width=143, height=41, bg='#FFFFFF')
colorcodebox = Entry(root, textvariable=colcode, font=entryfont, relief=FLAT, width=9, justify=CENTER, bg='#252525', fg='white')

colorboxframe.place(x=78, y=148)
getcolorbuttonframe.place(x=78, y=88)
colorcodebox.place(x=80, y=150)
getcolorbutton.place(x=80, y=90)

getcolorbutton.bind('<Enter>', e_getcolor)
getcolorbutton.bind('<Leave>', l_getcolor)

Rboxframe = Frame(root, width=63, height=32, bg='#FFFFFF')
Gboxframe = Frame(root, width=63, height=32, bg='#FFFFFF')
Bboxframe = Frame(root, width=63, height=32, bg='#FFFFFF')

rc = IntVar()
gc = IntVar()
bc = IntVar()

RLabel = Label(root, text='R:', bg='#252525', font=labelfont, fg='white')
RBox = Entry(root, textvariable=rc, width=5, font=rgbentryfont, justify=CENTER, relief=FLAT, bg='#252525', fg='white')
GLabel = Label(root, text='G:', bg='#252525', font=labelfont, fg='white')
GBox = Entry(root, textvariable=gc, width=5, font=rgbentryfont, justify=CENTER, relief=FLAT, bg='#252525', fg='white')
BLabel = Label(root, text='B:', bg='#252525', font=labelfont, fg='white')
BBox = Entry(root, textvariable=bc, width=5, font=rgbentryfont, justify=CENTER, relief=FLAT, bg='#252525', fg='white')

Rboxframe.place(x=131, y=231)
Gboxframe.place(x=131, y=281)
Bboxframe.place(x=131, y=331)

RLabel.place(x=103, y=230)
RBox.place(x=133, y=233)
GLabel.place(x=103, y=280)
GBox.place(x=133, y=283)
BLabel.place(x=103, y=330)
BBox.place(x=133, y=333)

rc.set(255)
gc.set(255)
bc.set(255)

while True:
        root.update()
        colcode.set(gethexbyrgbvar(rc.get(), gc.get(), bc.get()))
        RBox.config(fg=getr(rc.get()))
        GBox.config(fg=getg(gc.get()))
        BBox.config(fg=getb(bc.get()))
        colorboxframe.update()

