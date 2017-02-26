#Author:Siladittya Manna
#Date:2/26/2017
import Tkinter as tk
import tkFileDialog
import os,math
from PIL import Image
global filepath
main = tk.Tk()
main.title('Image Resizer')
main.iconbitmap(r'love.ico')
ws,hs = main.winfo_screenwidth(),main.winfo_screenheight()
def getpath(event):
    global filepath
    filepath = openpath()
def openpath():
    filename = tkFileDialog.askopenfilename(title='Choose Image')
    if filename != None:
        print 'Success'
        print filename
        #filepath = filename
        file_name.set(filename)
        return filename
def ImageResize(event):
    try:
        picw = int(math.floor(float(owidth.get())*37.795275591))
        pich = int(math.floor(float(oheight.get())*37.795275591))
        print picw,pich
    except:
        print "Enter valid Dimensions..."
    #print picw,pich
    #Image Resizing
    try:
        src = Image.open(filepath)
    except:
        print "File Error..."
    pathname = os.path.abspath(filepath)
    try:
        path = pathname.split('\\')
    except:
        path = pathname.split('/')
    fname = path[-1].split('.')[0]
    dirname = '/'.join(path[:-1])
    fname = fname+'NEW'+'.'+'jpeg'
    imgo = '/'.join([dirname,fname])
    #print pathname
    #print path
    #print fname
    #print dirname
    #print imgo
    dst = src.resize((picw,pich))
    dst.save(imgo,"JPEG")
#main.overrideredirect(1)
label = tk.LabelFrame(main,text = 'WorkSpace')
label.configure(background = 'blue')
label.grid(column=0,row=0,padx=10,pady=10,sticky='NSEW')
file_name = tk.StringVar(None)

inputfile = tk.Label(label,text = 'Enter Input File: ')
inputfile.grid(column=0,row=0,padx=10,pady=10,sticky='W')
ifilename = tk.Entry(label,textvariable=file_name)
ifilename.grid(column=1,row=0,padx=10,pady=10,sticky='E')
ibutton = tk.Button(label,text = 'Browse',command = getpath)
ibutton.grid(column=2,row = 0,padx=10,pady=10,sticky='E')
ibutton.bind('<Button-1>',getpath)

width = tk.Label(label,text = 'Enter Width(in cm): ')
width.grid(column=0,row=1,padx=10,pady=10,sticky='W')
owidth = tk.Entry(label)
owidth.grid(column=0,row=2,padx=10,pady=10,sticky='E')

height = tk.Label(label,text = 'Enter Height(in cm): ')
height.grid(column=1,row=1,padx=10,pady=10,sticky='W')
oheight = tk.Entry(label)
oheight.grid(column=1,row=2,padx=10,pady=10,sticky='E')

Okbutton = tk.Button(label,text = 'Press C',command = ImageResize)
Okbutton.grid(columnspan = 3,padx=10,pady=10,sticky='WE')
Okbutton.bind('c',ImageResize)

main.mainloop()
#37.795275591
