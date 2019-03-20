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



def create_gif_from_png(pathIn, pathOut):
    """ 
    pathIn: directory where are .png files
    pathOut: directory where .gif file is created
    """
    arr = os.listdir(pathIn)
    arr.sort()
    print(arr)

    with imageio.get_writer(pathOut+str('/Map.gif'), mode='I', duration=0.9) as writer:
        for i in arr:
            if (i.endswith('.png')):
                print(i)
                image = imageio.imread(pathIn+(i))
                writer.append_data(image)          
    return




if __name__ == "__main__":

    pathIn = "/home/gag/Escritorio/nuevasInunadaciones/histograms/"
    pathOut = "/home/gag/Escritorio/nuevasInunadaciones/histograms/"
    create_gif_from_png(pathIn, pathOut)


