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

mainapp = tkinter.Tk()
mainapp.title("Rick or Morty ?")

screen_x = int(mainapp.winfo_screenwidth())
screen_y = int(mainapp.winfo_screenheight())
window_x = 1000
window_y = 800

posX = (screen_x // 2)-(window_x // 2)
posY = (screen_y // 2)-(window_y // 2)

geo = "{}*{}+{}+{}".format(window_x,window_y,posX,posY)

mainapp.mainloop(geo)
