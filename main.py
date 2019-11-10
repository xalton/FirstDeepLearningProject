#coding:utf-8
#!/usr/bin/env python
import os
import time
import tkinter as tk
import numpy as np
import pandas as pd
import tensorflow as tf

import tkinter.font as tkFont
from PIL import ImageTk, Image
from matplotlib import pyplot as plt
from tensorflow.keras.callbacks import TensorBoard
from functions import DataPreparation,PlotImages,CreateModel
from tensorflow.keras.preprocessing.image import ImageDataGenerator

###Functions###

def resize_image(event):
    new_width = event.width
    new_height = event.height

    image = bg.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)

    bg_label.config(image=photo)
    bg_label.image = photo  # avoid garbage collection

def name_func():
    print('Test')

def close_window ():
    root.destroy()


path = '/home/machinelearning/Documents/FirstDeepLearningProject/'
###SetUp Window###
root = tk.Tk()
title = "Rick or Morty ?"
root.title(title)
img = tk.PhotoImage(file=path+'Images/rick.png')
root.tk.call('wm', 'iconphoto', root._w, img)

screen_x, screen_y = 1000,600
geo = "%dx%d" % (screen_x, screen_y)
root.minsize(800,600)
root.maxsize(1920,1080)
root.geometry(geo)

frame = tk.Frame(root, relief='raised', borderwidth=2)
frame.pack(fill='both', expand= True)
frame.pack_propagate(False)

bg = Image.open(path+"Images/bg1.png")
photo = ImageTk.PhotoImage(bg)


bg_label = tk.Label(frame,
        image=photo,
        text=title,
        anchor='nw',
        compound='bottom',
        font='courier 90',
        )

bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.bind('<Configure>',resize_image)

btn_h = 1
btn_w = 6
button_train = tk.Button(frame, text='Train',
        bg='#e8ff95',
        font=('courier',25),
        command=name_func,
        height = btn_h,
        width = btn_w,
         )
button_test = tk.Button(frame, text='Test',
        bg='#e8ff95',
        font=('courier',25),
        command=name_func,
        height = btn_h,
        width = btn_w,
         )
button_quit = tk.Button(frame, text='Quit',
        bg='#e8ff95',
        font=('courier',25),
        command=close_window,
        height = btn_h,
        width = btn_w,
         )

button_train.place(relx=0.5, rely=0.23, anchor='center')
button_test.place(relx=0.5, rely=0.35, anchor='center')
button_quit.place(relx=0.5, rely=0.47, anchor='center')
root.mainloop()



#Input name
#entry_name = tkinter.Entry(root,width=25)
#entry_name.pack()

#Button
#button_Test = tkinter.Button(root, text='Test',command = name_func)

#Check
#check_widget = tkinter.Checkbutton(root,text='')
#check_widget.pack()

#cursor/spinbox/listbox
#lb = tk.Listbox(root)
#lb.insert(1,"")
#scale_w = tk.Scale(root,from_=10,to=100,tickinterval=25)
#spin_w = tk.spinbox(root, from_=1,to=10)
#lb.pack()
#spin_w.pack()
#scale_w.pack()

#error
#from tkinter import messagebox
#messagebox.showerror(...)
#put on a button

#variable
#tkinter.StringVar()
#IntVar,DoubleVar,BoolVar
#create a label..:BE
# textvariable or variable
#var_label.set()

#Observeur
#def update_label(*args):
#   var_label.set(var_entry.get())
#var_entry.trace("w",update_label)

#using grid instead of pack()
