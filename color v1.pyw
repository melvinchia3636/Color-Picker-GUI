from PIL import ImageGrab
from tkinter import *
from tkinter.font import Font

def getcoor(event):
    global point
    point = root.winfo_pointerxy()
    print(point)
    root.unbind('<Button-1>')
    root.attributes("-fullscreen", False)
    root.config(bg='#252525')
    root.attributes('-alpha', 1.0)
    root.config(cursor='arrow')
    getcolor()
    

def getcolor():
    global point
    global colorcode
    px=ImageGrab.grab().load()
    color=px[point[0],point[1]]
    hexr = str(hex(rc.get())).replace('0x', '')
    hexg = str(hex(gc.get())).replace('0x', '')
    hexb = str(hex(bc.get())).replace('0x', '')
    print(color)
    if hexr == '0':
        hexr = '00'
    if hexg == '0':
        hexg = '00'
    if hexb == '0':
        hexb = '00'
    if len(hexr) == 1:
        hexr = '0'+hexr
    if len(hexg) == 1:
        hexr = '0'+hexg
    if len(hexb) == 1:
        hexr = '0'+hexb

    colorboxframe.place(x=85.5, y=88)
    getcolorbuttonframe.place(x=84, y=148)
    colorcodebox.place(x=87.5, y=90)
    getcolorbutton.place(x=86, y=150)

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
    global colorcode
    
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
    
    root.attributes("-fullscreen", True)
    root.config(bg='white')
    root.attributes('-alpha', 0.01)
    root.config(cursor='crosshair')
    root.bind('<Button-1>', getcoor)
    root.update()

root = Tk()
root.geometry('300x400')
root.title('Color Picker')
root.config(bg='#252525')
root.resizable(False, False)

def e_getcolor(event):
    getcolorbutton['bg'] = '#565656'
    getcolorbutton['fg'] = 'white'
def l_getcolor(event):
    getcolorbutton['bg'] = '#252525'
    getcolorbutton['fg'] = 'white'

buttonfont = Font(size=15, family='Bahnschrift SemiBold')
entryfont = Font(size=20, family='Bahnschrift Light')
labelfont = Font(size=15, family='Bahnschrift SemiBold')
rgbentryfont = Font(size=15, family='Bahnschrift Light')
titlefont = Font(size=30, family='Bahnschrift SemiBold')

getcolorbuttonframe = Frame(root, width=143, height=46, bg='#FFFFFF')
getcolorbutton = Button(
    root,
    text='PICK COLOR',
    command=startgetcoor,
    relief=FLAT,
    font=buttonfont,
    bg='#252525',
    fg='white',
    activebackground='#565656',
    activeforeground='white',
    width=11,
    padx=5
    )

colcode = StringVar()

title = Label(root, text='COLOR PICKER',font=titlefont, bg='#252525', fg='white')
title.place(x=10, y=10)

colorboxframe = Frame(root, width=143, height=41, bg='#FFFFFF')
colorcodebox = Entry(root, textvariable=colcode, font=entryfont, relief=FLAT, width=9, justify=CENTER, bg='#252525', fg='white')

colorboxframe.place(x=78, y=88)
getcolorbuttonframe.place(x=78, y=148)
colorcodebox.place(x=80, y=90)
getcolorbutton.place(x=80, y=150)

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
    try:
        root.update()
        try:
            hexr = str(hex(rc.get())).replace('0x', '')
            hexg = str(hex(gc.get())).replace('0x', '')
            hexb = str(hex(bc.get())).replace('0x', '')
            if hexr == '0':
                hexr = '00'
            if hexg == '0':
                hexg = '00'
            if hexb == '0':
                hexb = '00'
            if len(hexr) == 1:
                hexr = '0'+hexr
            if len(hexg) == 1:
                hexg = '0'+hexg
            if len(hexb) == 1:
                hexb = '0'+hexb
            colcode.set('#'+ (str(hexr) + str(hexg) + str(hexb)).upper())
            RBox.config(fg='#'+(str(hexr)+'0000'))
            GBox.config(fg='#'+'00'+(str(hexg)+'00'))
            BBox.config(fg='#'+'0000'+(str(hexb)))
            colorboxframe.update()
        except:
            root.update()
    except:
        pass
