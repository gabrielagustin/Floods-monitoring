# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 14:46:41 2018

@author: gag

Script que permite realizar la detección de áreas inundadas en imágenes SAR,
para lo cual se ajusta una función multimodal al histograma de cada imagen SAR
y de esta función se obtienen obtienen estadisticos que permiten realizar
la discriminación de las zonas. 

"""
import os
from matplotlib import cm
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


import functions

# from pylab import *
# #from mpl_toolkits.axes_grid1 import ImageGrid

# import matplotlib.cm as cm
# from skimage import io


# #from scipy import stats

# from scipy import stats
# 
# import seaborn as sns
# from PIL import Image
# #import imageio
# from numpy import linspace
# from mpl_toolkits.axes_grid1 import make_axes_locatable
# import numpy.ma as ma
# import pandas as pd
# from scipy import stats

# from pylab import *

# from sklearn.mixture import GaussianMixture
# import scipy.stats

# from copy import deepcopy


# import peakutils
# from peakutils.plot import plot as pplot


# from scipy import ndimage as nd
# from skimage.morphology import watershed, square


##### Sentinel S1A-2015-2016 -- Inundacion
path = "/media/gag/Datos/Estancia_Italia_2018/Sentinel-1A-SantaFe/Recorte_dB/"
pathMapas = "/media/gag/Datos/Trabajos/Sentinel-1A-SantaFe/Mapas/"


##### Sentinel S1B
#path = "/media/stanza/DA6EF09D6EF0741B/Sentinel1B-SantaFe/Recorte_dB/"



arr = os.listdir(path)
### ordeno la lista
arr.sort()
print(arr)

# Fit GMM
#gmm = GaussianMixture(n_components = 3)
#gmm = gmm.fit(hist)

my_cmap1 = cm.gray
my_cmap1.set_under('k',alpha=0)
#my_cmap1 = cm.Greens
my_cmap2 = cm.Blues_r
my_cmap2.set_under('k',alpha=0)
my_cmap3=cm.Greens_r
my_cmap3.set_under('k',alpha=0)
my_cmap4=cm.Reds_r
my_cmap4.set_under('k',alpha=0)
my_cmap5=cm.Oranges_r
my_cmap5.set_under('k',alpha=0)




fig, ax = plt.subplots()

for i in arr:
#    S1A
#    i = "20150427.data"
    i = "20150109.data"
#    i = "20150521.data"
#    i = "20150403.data"
#    i = "20160207.data" 
#    i = "20160326.data"
#    i = "20160419.data"
#    S1B
#    i = "20161010.data"
#    plt.clf()
    print(i)
    
#    ax.cla()
    path2 = path + i
    fileVV = path2 +"/Sigma0_VV_db.img"
    ### se lee la imagen
    src_ds_VV, bandVV, GeoTVV, ProjectVV = functions.openFileHDF(fileVV, 1)
    transform = GeoTVV
    src_ds_VV = src_ds_VV
    xmin,xmax,ymin,ymax=transform[0],transform[0]+transform[1]*src_ds_VV.RasterXSize,transform[3]+transform[5]*src_ds_VV.RasterYSize,transform[3]
    ### se calcula y se plotea el histograma
    lcNew = bandVV.flatten('C')
    y, x, _= plt.hist(lcNew, 400, [-30,-1], facecolor='gray', normed=1) 
    
    fecha = i[:-5]
    plt.title(fecha)
    plt.xlim(-30, -1)
    plt.ylim(0, 0.3)

    ### se calcula los valores en el eje x para los cuales se producen los 
    ### máximos en el histograma
    x= x[:-1]
    pico1, minimoLocal, pico2, pico3 = functions.Max1MinLocalMax2(x,y)
    
    #### para cada máximo se escriben los valores en la gráfica
    ind = np.where(x==pico1)[0]
    y_i = float(y[ind])
    print(y_i)
    texto = '('+ str(np.round(pico1,2))+';'+str(np.round(y_i,2))+')'
    plt.text(pico1+pico1/10, y_i+y_i/10, texto)

    ind = np.where(x==pico2)[0]
    y_i = float(y[ind])
    print(y_i)
    texto = '('+ str(np.round(pico2,2))+';'+str(np.round(y_i,2))+')'
    plt.text(pico2+pico2/10, y_i+y_i/10, texto)

    plt.show()     

# ##------------------------------------------------------------------------------  

#     if(pico2 != pico3):
#             ind = np.where(x==pico3)[0]
#             y_i = float(y[ind])
#             print(y_i)
#             texto = '('+ str(np.round(pico3,2))+';'+str(np.round(y_i,2))+')'
#             plt.text(pico3+pico3/10, y_i+y_i/10, texto)


    
#     expected=(pico1,0.5,0.05,pico2,0.5,0.2,pico3,0.5,0.2)
#     params,cov=curve_fit(bimodal, x, y, expected, maxfev=750000)
#     sigma=sqrt(diag(cov))
#     plot(x[:-1],bimodal(x[:-1],*params),color='red',lw=1,label='model')
#     plt.legend()
#     new = pd.DataFrame(data={'params':params},index=bimodal.__code__.co_varnames[1:])
#     print(new)
#     mu1 = new.params[0]
#     sigma1 = new.params[1]

#     mu2 = new.params[3]
#     sigma2 = np.abs(new.params[4])

#     mu3 = new.params[6]
#     sigma3 = new.params[7]
    
# #    
#     fecha = i[:-5]
#     fig, ax = plt.subplots()
    
# #    plt.title(fecha)   
# #
# #    ax.yaxis.set_major_locator(plt.MaxNLocator(4))
# #    ax.xaxis.set_major_locator(plt.MaxNLocator(4))
# #    divider = make_axes_locatable(ax)  
# #    plt.title(fecha)   
# #    
# #    
# ##    distance = nd.distance_transform_edt(bandVV == 0)
# ##    result = watershed(distance, bandVV, mask=bandVV,
# ##                   connectivity=square(3))
# ##    bandVV = result
# #
# #    ######---------------------------------------------------------------------    
# #    #### se aplica la umbralizacion utilizando los valores ohttp://www.bna.com.ar/Personas/HomeBankingbtenidos del 
# #    #### ajuste de la funcion multimodal al histograma
# #    ### for ciudad
#     thresholdedCity = deepcopy(bandVV)
#     thresholdedCity[thresholdedCity < -5] = 0
#     thresholdedCity[thresholdedCity > 5] = 0   
# #    thresholdedCity[thresholdedCity != 0] = 1
     
#     ### for water
#     thresholdedW = deepcopy(bandVV)
#     thresholdedW[thresholdedW > mu1 + sigma1] = 0
#     thresholdedW[thresholdedW < mu1 - sigma1] = 0 
# #    thresholdedW[thresholdedW != 0] = 1
    
#     ### for vegetated areas
#     thresholdedV = deepcopy(bandVV)
#     thresholdedV[thresholdedV > mu3 + sigma3] = 0
#     thresholdedV[thresholdedV < mu3 - sigma3] = 0
# #    thresholdedV[thresholdedV != 0] = 1
        
#     # for third max
#     thresholdedNew = deepcopy(bandVV)
#     thresholdedNew[thresholdedNew > mu2 + sigma2] = 0
#     thresholdedNew[thresholdedNew < mu2 - sigma2] = 0   
# #
# #    ######--------------------------------------------------------------------- 
# #    ###### se plotean los mapas de inundacion con tres clases
# #    ##### Vegetacion-Agua-Tercer clase#for x in range(subwin_size, w-subwin_size,subwin_size):
# ##    for y in range(subwin_size, h-subwin_size,subwin_size):    
# ##        print(y-subwin_size)
# ##        print(y+subwin_size)
# ##        print(x-subwin_size)
# ##        print(x+subwin_size)
# ###        iy = y-subwin_size
# ###        jy = y+subwin_size
# ###        ix = x-subwin_size
# ###        jx = x+subwin_size
# ##        subwin = bandVV[x-subwin_size:x+subwin_size, y-subwin_size:y+subwin_size]
# ###        hist = genHist(subwin)         # Generate histogram
# ##        fig, ax = plt.subplots()
# ##        plt.imshow(subwin)
# ##        lcNew = subwin.flatten('C')
# ##        fig, ax = plt.subplots()
# ##        yy, xx, _= plt.hist(lcNew,500, [-30,-1], facecolor='gray', normed=1) 
# ####        plt.xlim(-30, -1)
# ####        plt.ylim(0, 0.3)
# ##        plt.show()
# ###        
# ###        plt.pause(5)
# #   
# #    ### se aplican los centroide y los desvios de la funcion multimodal encontrada
# #    ### para clasificar la imagen satelital
# #    #### la primer guasiana representa agua libre
# #   
# #    coeff = 2.5   
# #   
# #    r1 =(mu1-sigma1*coeff)
# ##    print(r1)
# #    r2 = (mu1+sigma1*coeff)
# ##    print(r2)
# #    print("Agua:"+str([r1,r2]))
# #    #### la gausiana intermedia representa la transicion entre agua y suelo vegetado
# #    im0 = ax.imshow(bandVV, extent=[xmin,xmax,ymin,ymax], cmap=my_cmap2, vmin=r1, vmax=r2, interpolation="Bilinear")
# #    r3 = (mu2-sigma2*coeff)
# ##    print(r3)
# #    r4 = (mu2+sigma2*coeff)
# ##    print(r4)  
# #    print("Transicion:"+str([r3,r4]))
# #    im1 = ax.imshow(bandVV, extent=[xmin,xmax,ymin,ymax], cmap=my_cmap5, vmin=r3, vmax=r4, interpolation="Bilinear")
# #    ### la tercer gausiana representa suelo/vegetacion
# #    r5 = (mu3-sigma3*coeff)
# ##    print(r5)
# #    r6 = (mu3+sigma3*coeff)
# ##    print(r6)  
# #    print("Vegetacion/suelo:"+str([r5,r6]))
# #    im2 = ax.imshow(bandVV, extent=[xmin,xmax,ymin,ymax], cmap=my_cmap3, vmin=r5, vmax=r6, interpolation="Bilinear")
# #    ### se identifican ciudades
# #    r7 = -6
# #    r8 = 5
# #    print("Ciudades:"+str([r7,r8]))
# #    im3 = ax.imshow(bandVV, extent=[xmin,xmax,ymin,ymax], cmap=my_cmap1, vmin=r7, vmax=r8, interpolation="Bilinear")
# #    # Build the colorbar on the right
# #    # Place a colorbar next to the map
# #    cbar = fig.colorbar(im0, ticks=[-1, 0, 1], orientation='horizontal')
# #    cbar = fig.colorbar(im1, ticks=[-1, 0, 1], orientation='horizontal')
# ##    cbar = im0.colorbar(im0, 'right', size='5%', pad='5%')
# #    # Build the colorbar on the bottom
# #    # cbar = m.colorbar(im, 'bottom', size='5%', pad='8%')
# ##    cbar.set_label('Degrees C')
# # 
# ##------------------------------------------------------------------------------  
# #     
     
# #    r1 = int(np.round(mu1-sigma1))
# #    print(r1)
# #    r2 = int(np.round(mu1+sigma1))
# #    print(r2)
#     img0 = ax.imshow(bandVV,extent=[xmin,xmax,ymin,ymax], cmap=my_cmap1, interpolation="Bilinear")
# #    rango = list(range(r1, r2, 2))
# #    print(rango)    
# ##    ax.contourf(bandVV, cmap=my_cmap2, levels = rango)
# #    r3 = int(np.round(mu2-sigma2))
# #    print(r3)
# #    r4 = int(np.round(mu2+sigma2))
# #    print(r4)  
# #   
# #    rango = list(range(r3, r4, 2))
# #    print(rango)
# #    ax.contourf(bandVV, cmap=my_cmap3, levels = rango)
# #    r5 = int(np.round(mu3-sigma3))
# #    print(r5)
# #    r6 = int(np.round(mu3+sigma3))
# #    print(r6)  
# #    
# #    rango = list(range(r5, r6, 1))
# #    print(rango)
# #    ax.contourf(bandVV, cmap=my_cmap1, levels = rango)    
# #    
    
#     img1 = ax.imshow(thresholdedV,extent=[xmin,xmax,ymin,ymax], cmap=my_cmap3, interpolation="Bilinear")
   
#     water = np.ma.masked_where(thresholdedV != 0, thresholdedW) 
#     img2 = ax.imshow(water,extent=[xmin,xmax,ymin,ymax], cmap=my_cmap2, interpolation="Bilinear")
    
#     thresholdedV = deepcopy(bandVV)
# #    thresholdedCity[thresholdedCity != 0] = 1
# #    img3 = ax.imshow(thresholdedCity,extent=[xmin,xmax,ymin,ymax], cmap=my_cmap4, interpolation="Bilinear")
#     city = np.ma.masked_where(water!= 0, thresholdedCity)        
#     img3 = ax.imshow(city,extent=[xmin,xmax,ymin,ymax], cmap=my_cmap4, interpolation="Bilinear")

#     New = np.ma.masked_where(city != 0, thresholdedNew)
#     thresholdedNew[thresholdedNew != 0] = 1
#     img4 = ax.imshow(New,extent=[xmin,xmax,ymin,ymax], cmap=my_cmap1, interpolation="Bilinear")
    
#     ax.yaxis.set_major_locator(plt.MaxNLocator(5))
#     ax.xaxis.set_major_locator(plt.MaxNLocator(5))
#     ax.xaxis.tick_top()
# #    plt.savefig(str(pathMapas) + str(fecha) +'.png')
# #    plt.pause(3)
# #--------------------------------------------------------------------------
#     plt.show()



# #data=concatenate((normal(1,.2,5000),normal(2,.2,2500)))
# #y,x,_=hist(data,100,alpha=.3,label='data')
# #
# #x=(x[1:]+x[:-1])/2 # for len(x)==len(y)
# #
# #
# #expected=(1,.2,250,2,.2,125)
# #params,cov=curve_fit(bimodal,x,y,expected)
# #sigma=sqrt(diag(cov))
# #plot(x,bimodal(x,*params),color='red',lw=3,label='model')
# #legend()
# #plt.show()
# #new = pd.DataFrame(data={'params':params,'sigma':sigma},index=bimodal.__code__.co_varnames[1:])
# #
# #print(new)




# ###### codigo para mostrar los histogramas superpuestos
# #fig, ax = plt.subplots()
# #
# #for i in arr:
# #    print(i)
# #    ax.cla()
# #    fileVV = path + "20150109.data" +"/Sigma0_VV_db.img"
# #    src_ds_VV_0, bandVV_0, GeoTVV_0, ProjectVV_0 = functions.openFileHDF(fileVV, 1)
# #    transform = GeoTVV_0
# #    src_ds_VV = src_ds_VV_0
# #    xmin,xmax,ymin,ymax=transform[0],transform[0]+transform[1]*src_ds_VV.RasterXSize,transform[3]+transform[5]*src_ds_VV.RasterYSize,transform[3]
# #    lcNew_0 = bandVV_0.flatten('C')
# #    y, x, _= plt.hist(lcNew_0, 500, [-30,-1], facecolor='gray', normed=1) 
# #    
# #    #fecha = i[:-5]
# #    #plt.title(fecha)
# #    plt.xlim(-30, -1)
# #    plt.ylim(0, 0.3)
# #
# #    if (i != "20150109.data"):
# #        path2 = path + i
# #        fileVV = path2 +"/Sigma0_VV_db.img"
# #        src_ds_VV, bandVV, GeoTVV, ProjectVV = functions.openFileHDF(fileVV, 1)
# #        transform = GeoTVV
# #        src_ds_VV = src_ds_VV
# #        xmin,xmax,ymin,ymax=transform[0],transform[0]+transform[1]*src_ds_VV.RasterXSize,transform[3]+transform[5]*src_ds_VV.RasterYSize,transform[3]
# #    
# #        lcNew = bandVV.flatten('C')
# #        y_i, x_i, _= plt.hist(lcNew, 500, [-30,-1], normed=1, facecolor='g', alpha=0.75) 
# # 
# #        fecha = i[:-5]
# #        plt.savefig(str("/home/stanza/Downloads/nuevasInunadaciones/Recorte_dB/") + str(fecha) +'.png')
# #        plt.show()






