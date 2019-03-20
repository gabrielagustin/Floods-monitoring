# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
Created on Tue Feb  5 10:58:49 2019

@author: gag

Script que genera una imagen .gif a partir de una compilación
de imagenes .png
 
"""


import os
import imageio


pathMap = "/home/gag/Escritorio/nuevasInunadaciones/histograms/"
arr = os.listdir(pathMap)
arr.sort()
print(arr)

with imageio.get_writer(pathMap+str('/Map.gif'), mode='I', duration=0.9) as writer:
    for i in arr:
        if (i.endswith('.png')):
            print(i)
            image = imageio.imread(pathMap+(i))
            writer.append_data(image)



