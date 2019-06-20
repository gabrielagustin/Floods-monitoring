# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
Created on Thu Jun 28 14:46:41 2018

@author: gag

Script that allows to obtain the graph of the temporal evolution of the histogram of the SAR images.
In gray the histogram of the initial state appears and superimposed in green appears the other states.

"""

import os
from matplotlib import pyplot as plt
import functions


path = "/media/gag/Datos/Estancia_Italia_2018/Sentinel-1A-SantaFe/Recorte_dB/"
arr = os.listdir(path)
### ordeno la lista
arr.sort()
print(arr)


##### codigo para mostrar los histogramas superpuestos
fig, ax = plt.subplots()

for i in arr:
   print(i)
   ax.cla()
   ### initial state
   fileVV = path + "20150109.data" +"/Sigma0_VV_db.img"
   src_ds_VV_0, bandVV_0, GeoTVV_0, ProjectVV_0 = functions.openFileHDF(fileVV, 1)
   transform = GeoTVV_0
   src_ds_VV = src_ds_VV_0
   xmin,xmax,ymin,ymax=transform[0],transform[0]+transform[1]*src_ds_VV.RasterXSize,transform[3]+transform[5]*src_ds_VV.RasterYSize,transform[3]
   ### se agrega fecha del la imagen
   fecha = i[:-5]
   plt.title(fecha)
   lcNew_0 = bandVV_0.flatten('C')
   y, x, _= plt.hist(lcNew_0, 500, [-30,-1], facecolor='gray', normed=1, label="20150109") 
   
   plt.xlim(-30, -1)
   plt.ylim(0, 0.3)

   if (i != "20150109.data"):
       ### for other states
       fecha = i[:-5]
       path2 = path + i
       fileVV = path2 +"/Sigma0_VV_db.img"
       src_ds_VV, bandVV, GeoTVV, ProjectVV = functions.openFileHDF(fileVV, 1)
       transform = GeoTVV
       src_ds_VV = src_ds_VV
       xmin,xmax,ymin,ymax=transform[0],transform[0]+transform[1]*src_ds_VV.RasterXSize,transform[3]+transform[5]*src_ds_VV.RasterYSize,transform[3]
   
       lcNew = bandVV.flatten('C')
       y_i, x_i, _= plt.hist(lcNew, 500, [-30,-1], normed=1, facecolor='g', alpha=0.75, label=fecha) 

       plt.legend()
       plt.savefig(str("/home/gag/Escritorio/nuevasInunadaciones/histograms/evolucion/") + str(fecha) +'.png')
       plt.show()

