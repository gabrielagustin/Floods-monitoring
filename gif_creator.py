# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
Created on Tue Feb  5 10:58:49 2019

@author: gag

Script que genera una imagen .gif a partir de una compilación
de imagenes .png o .img 
 
"""


import os
import imageio



def create_gif_from_png(pathIn, pathOut):
    """ 
    Generate .gif file using a .png files compilation
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


def create_gif_from_img(pathIn, pathOut):
    """ 
    Generate .gif file using a .img files compilation
        pathIn: directory where are .png files
        pathOut: directory where .gif file is created
    """
    #pathHistogramas = "/home/stanza/Downloads/nuevasInunadaciones/Recorte_dB/"
    pathMapasInu = "/home/stanza/Downloads/nuevasInunadaciones/Mapas/"
    with imageio.get_writer('/home/stanza/Mapas.gif', mode='I', duration=0.9) as writer:
        for i in arr:
            if (i.endswith('.png')):
                print(i)
            path2 = path + i
    #        fileVV = path2 +"/Sigma0_VV_db.img"
    #        fileVV = i
            src_ds_VV, bandVV, GeoTVV, ProjectVV = functions.openFileHDF(fileVV, 1)
    #        im = plt.imshow(bandVV)
    #        +"Histograma_"
    #        image = imageio.imread(pathHistogramas+(i))
            image = imageio.imread(pathMapasInu+(i))
            writer.append_data(image)
        
    #    
#    



if __name__ == "__main__":

    # pathIn = "/home/gag/Escritorio/nuevasInunadaciones/histograms/"
    # pathOut = "/home/gag/Escritorio/nuevasInunadaciones/histograms/"
    # pathIn = pathOut = "/home/gag/Escritorio/nuevasInunadaciones/Mapas/"
    pathIn = pathOut = "/home/gag/Escritorio/nuevasInunadaciones/SoloAgua/"
    create_gif_from_png(pathIn, pathOut)


