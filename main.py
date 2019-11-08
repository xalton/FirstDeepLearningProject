#coding:utf-8
#!/usr/bin/env python
import os
import time
import tkinter
import numpy as np
import pandas as pd
import tensorflow as tf
from matplotlib import pyplot as plt
from tensorflow.keras.callbacks import TensorBoard
from functions import DataPreparation,PlotImages,CreateModel
from tensorflow.keras.preprocessing.image import ImageDataGenerator

###SetUp Main Window###
mainapp = tkinter.Tk()
title = "Rick or Morty ?"
mainapp.title(title)

screen_x = int(mainapp.winfo_screenwidth())
screen_y = int(mainapp.winfo_screenheight())
window_x = 1000
window_y = 800

posX = (screen_x // 2)-(window_x // 2)
posY = (screen_y // 2)-(window_y // 2)

geo = "{}x{}+{}+{}".format(window_x,window_y,posX,posY)
mainapp.minsize(800,600)
mainapp.maxsize(1920,1080)
mainapp.geometry(geo)

label_title = tkinter.Label(mainapp, text=title)
#font30 = "-family {DejaVu Sans} size 30 -weight normal"
label_title.configure(font= '30')




label_title.pack()
mainapp.mainloop()



#Input name
#entry_name = tkinter.Entry(mainapp,width=25)
#entry_name.pack()

#Button
#button_Test = tkinter.Button(mainapp, text='Test',command = name_func)

#Check
#check_widget = tkinter.Checkbutton(mainapp,text='')
#check_widget.pack()
