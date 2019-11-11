#coding:utf-8
#!/usr/bin/env python
import os
import time
import tkinter as tk
import numpy as np
import pandas as pd
import tensorflow as tf

import tkinter.font as tkFont
from tkinter import ttk
from PIL import ImageTk, Image
from matplotlib import pyplot as plt
from tensorflow.keras.callbacks import TensorBoard
from functions import DataPreparation,PlotImages,CreateModel
from tensorflow.keras.preprocessing.image import ImageDataGenerator

path = '/home/machinelearning/Documents/FirstDeepLearningProject/'
###Style and Font###
font_title = ('courier',85)
def set_style():
    style = ttk.Style()
    style.theme_create( "st_app", parent="alt", settings={
#         "TLabel":        {"configure": {"foreground"      : StColors.bright_green,
#                                         "padding"         : 10,
#                                         "font"            : ("Calibri", 12)}},
#
#         "TCombobox":     {"configure": {"selectbackground": StColors.dark_grey,
#                                         "fieldbackground" : "white",
#                                         "background"      : StColors.light_grey,
#                                         "foreground"      : "black"}},
#
         "TButton":       {"configure": {"font"            :("courier", 25, 'bold'),
                                         "background"      : "#86C6CF",
                                         "foreground"      : "#192650",
                                         "relief"          : "raised",
                                         "anchor"          : "center"},
                             "map"      : {"background"      : [("active", '#86C6CF')],
                                         "foreground"      : [("active", '#D3F698')]}},
#
#         "TEntry":        {"configure": {"foreground"      : "black"}},
#         "Horizontal.TProgressbar":{"configure": {"background": StColors.mid_grey}}
    })
    style.theme_use("st_app")
    #style.configure('TButton', font =('courier', 20, 'bold'),borderwidth = '4')
    #style.map('TButton', foreground = [('active', '! disabled', 'green')],
#                      background = [('active', 'black')])

###SetUp Window###
class Application(tk.Tk):

    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.title("Rick or Morty ?")
        img = tk.PhotoImage(file=path+'Images/rick.png')
        self.tk.call('wm', 'iconphoto', self._w, img)
        self.minsize(800,600)
        self.maxsize(1920,1080)
        self.geometry("1000x600")
        set_style()

        container = tk.Frame(self)
        container.pack(side='top',fill='both',expand=True)
        container.pack_propagate(False)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage,TestPage,TrainPage):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky='nsew')
        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

###Setup Pages###
class ResizingLabel(tk.Label):
    def __init__(self, parent, imagepath, *args, **kwargs):
        tk.Label.__init__(self, parent, *args, **kwargs)

        self.configure(bd=0)
        self.parent=parent
        self.parent.bind('<Configure>', self._resize_image)

        self.imagepath = imagepath
        self.image = Image.open(self.imagepath)
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = tk.Label(self, image=self.background_image,
                        text=' Rick or Morty ?',
                        font=font_title,
                        foreground='#192650',
                        anchor='n',
                        compound='bottom',
                        justify='right')
        self.background.place(x=0,y=0, relwidth=1, relheight=1)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = self.parent.winfo_width()
        new_height = self.parent.winfo_height()

        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)

class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        bg_path = path+'/Images/bg1.png'
        bg_label = ResizingLabel(self, bg_path)
        btn_h = 35
        btn_w = 150
        button_train = ttk.Button(self, text='Train',
                    command=lambda:controller.show_frame(TrainPage))
        button_test = ttk.Button(self, text='Test',
                    command=lambda:controller.show_frame(TestPage))
        button_quit = ttk.Button(self, text='Quit',
                    command=lambda:app.destroy())

        bg_label.place(x=1, y=1, relwidth=1, relheight=1)
        button_train.place(relx=0.5, rely=0.23, anchor='center',
                    height=btn_h,
                    width=btn_w)
        button_test.place(relx=0.5, rely=0.35, anchor='center',
                    height=btn_h,
                    width=btn_w)
        button_quit.place(relx=0.5, rely=0.47, anchor='center',
                    height=btn_h,
                    width=btn_w)

class TrainPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Training page", font=('courier',12))
        label.pack(pady=10,padx=10)
        button_test1 = ttk.Button(self, text='Test',
                    command=lambda:controller.show_frame(TestPage))
        button_main1 = ttk.Button(self, text='Main',
                    command=lambda:controller.show_frame(StartPage))
        button_test1.pack()
        button_main1.pack()

class TestPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Test page", font=('courier',12))
        label.pack(pady=10,padx=10)
        button_main2 = ttk.Button(self, text='Main',
                    command=lambda:controller.show_frame(StartPage))
        button_train2 = ttk.Button(self, text='Back to training',
                    command=lambda:controller.show_frame(TrainPage))
        button_main2.pack()
        button_train2.pack()

###Run app###
app = Application()
app.mainloop()
# screen_x, screen_y = 1000,600
# geo = "%dx%d" % (screen_x, screen_y)
# root.minsize(800,600)
# root.maxsize(1920,1080)
# root.geometry(geo)
#
# frame = tk.Frame(root, relief='raised', borderwidth=2)
# frame.pack(fill='both', expand= True)
# frame.pack_propagate(False)
#
# bg = Image.open(path+"Images/bg1.png")
# photo = ImageTk.PhotoImage(bg)
#
#
# bg_label = tk.Label(frame,
#         image=photo,
#         text=title,
#         anchor='nw',
#         compound='bottom',
#         font='courier 90',
#         )
#
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)
# bg_label.bind('<Configure>',resize_image)
#
# btn_h = 1
# btn_w = 6
# button_train = tk.Button(frame, text='Train',
#         bg='#e8ff95',
#         font=('courier',25),
#         command=name_func,
#         height = btn_h,
#         width = btn_w,
#          )
# button_test = tk.Button(frame, text='Test',
#         bg='#e8ff95',
#         font=('courier',25),
#         command=name_func,
#         height = btn_h,
#         width = btn_w,
#          )
# button_quit = tk.Button(frame, text='Quit',
#         bg='#e8ff95',
#         font=('courier',25),
#         command=close_window,
#         height = btn_h,
#         width = btn_w,
#          )
#








#Input name
#entry_name = tkinter.Entry(root,width=25)
#entry_name.pack()

#Button
#button_Test = tkinter.Button(root, text='Test',command = name_func)
#        button_Test = tk.Button(self, text='Test',
#                    command=lambda:qf("Yes"))

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
