# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
Created on Tue Feb  5 10:58:49 2019

@author: gag

Script that generate an image .gif from a compilation images .png or .img
 
"""

import os
import imageio



def create_gif_from_png(pathIn, pathOut):
    """ Generate .gif file using a .png files compilation

    Parameters:
    -----------
    pathIn : complete path of the image to read
    pathOut : complete path of the image to be created

    Returns: 
    --------
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



def create_gif(pathIn, extImg, nameFileOut):
    """ Generate .gif file using a .img files compilation

    Parameters:
    -----------
    pathIn : complete path of drthe image to read
    extImg : type of image to read ".PNG", ".IMG"
    nameFileOut : name of the image to be created

    Returns: 
    --------
    """

    # list all files in the directory
    arr = os.listdir(pathIn)
    # sort the files using alfabetic names
    arr.sort()

    with imageio.get_writer(pathIn + '/' + nameFileOut, mode='I', duration=0.9) as writer:
        for i in arr:
            if(extImg == '.png'):                   
                if (i.endswith('.png')):
                    print(i)
                    image = imageio.imread(pathIn+(i))
                    writer.append_data(image)     
            if(extImg == '.img'):                   
                if (i.endswith('.img')):
                    print(i)
                    image = imageio.imread(pathIn+(i))
                    writer.append_data(image)     
    ## deberia saber si se modifico o si realmente se modifico el archivo de salida
    print("Archivo creado con exito!!!")
    return
                


if __name__ == "__main__":

    pathIn = pathOut = "/.../"
    create_gif_from_png(pathIn,  pathOut)

