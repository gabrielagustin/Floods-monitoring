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

# print( filter(lambda x: x.endswith('.png'), os.listdir(pathMap)))
# print(arr2)


# with imageio.get_writer(pathMap+str('/Mapas.gif'), mode='I', duration=0.9) as writer:
#     for i in arr:
#         if ()
#         print(i)
#         path2 = path + i
# #        fileVV = path2 +"/Sigma0_VV_db.img"
# #        fileVV = i
#         src_ds_VV, bandVV, GeoTVV, ProjectVV = functions.openFileHDF(fileVV, 1)
# #        im = plt.imshow(bandVV)
# #        +"Histograma_"
# #        image = imageio.imread(pathHistogramas+(i))
#         image = imageio.imread(pathMapasInu+(i))
#         writer.append_data(image)
    

