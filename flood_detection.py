# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
Created on Thu Jun 28 14:46:41 2018

@author: gag

Script that allows the detection of flooded areas in SAR images.
It adjusts a multimodal function to the histogram of each SAR image 
and from this function, statistics are obtained (statistics of each 
Gaussian function) that allow the discrimination of the zones.

"""
import os
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import functions


def multimodal_analysis(fileVV):
    ### se lee la imagen
    src_ds_VV, bandVV, GeoTVV, ProjectVV = functions.openFileHDF(fileVV, 1)
    transform = GeoTVV
    src_ds_VV = src_ds_VV
    xmin,xmax,ymin,ymax=transform[0],transform[0]+transform[1]*src_ds_VV.RasterXSize,transform[3]+transform[5]*src_ds_VV.RasterYSize,transform[3]
    ### se calcula y se plotea el histograma
    lcNew = bandVV.flatten('C')
    fig, ax = plt.subplots()
    y, x, _= plt.hist(lcNew, 400, [-30,-1], facecolor='gray', density=1) 
    fecha = i[:-5]
    plt.title(fecha)
    plt.xlim(-30, -1)
    plt.ylim(0, 0.3)


    peaks = functions.find_peaks(y)
    print("Maximos usando la funcion peaks: ")
    print(peaks)


#     ### se calcula los valores en el eje x para los cuales se producen los 
#     ### máximos en el histograma, los cuales pueden ser 2 o 3
    x= x[:-1]
    pico1, minimoLocal, pico2, pico3 = functions.Max1MinLocalMax2(x,y)
    
#     #### para cada máximo se escriben los valores en la gráfica
    ind = np.where(x==pico1)[0]
    y_i = float(y[ind])
#     print(y_i)
    texto = '('+ str(np.round(pico1,2))+';'+str(np.round(y_i,2))+')'
    plt.text(pico1+pico1/10, y_i+y_i/10, texto)

    ind = np.where(x==pico2)[0]
    y_i = float(y[ind])
    print(y_i)
    texto = '('+ str(np.round(pico2,2))+';'+str(np.round(y_i,2))+')'
    plt.text(pico2+pico2/10, y_i+y_i/10, texto)

    plt.show()     

# # ##------------------------------------------------------------------------------  

    # if(pico2 != pico3):
    #         ind = np.where(x==pico3)[0]
    #         y_i = float(y[ind])
    #         print(y_i)
    #         texto = '('+ str(np.round(pico3,2))+';'+str(np.round(y_i,2))+')'
    #         plt.text(pico3+pico3/10, y_i+y_i/10, texto)


    
# #     expected=(pico1,0.5,0.05,pico2,0.5,0.2,pico3,0.5,0.2)
# #     params,cov=curve_fit(bimodal, x, y, expected, maxfev=750000)
# #     sigma=sqrt(diag(cov))
# #     plot(x[:-1],bimodal(x[:-1],*params),color='red',lw=1,label='model')
# #     plt.legend()
# #     new = pd.DataFrame(data={'params':params},index=bimodal.__code__.co_varnames[1:])
# #     print(new)
# #     mu1 = new.params[0]
# #     sigma1 = new.params[1]

# #     mu2 = new.params[3]
# #     sigma2 = np.abs(new.params[4])

# #     mu3 = new.params[6]
# #     sigma3 = new.params[7]
    
# # #    
# #     fecha = i[:-5]
# #     fig, ax = plt.subplots()
    
# # #    plt.title(fecha)   
# # #
# # #    ax.yaxis.set_major_locator(plt.MaxNLocator(4))
# # #    ax.xaxis.set_major_locator(plt.MaxNLocator(4))
# # #    divider = make_axes_locatable(ax)  
# # #    plt.title(fecha)   
# # #    
# # #    
# # ##    distance = nd.distance_transform_edt(bandVV == 0)
# # ##    result = watershed(distance, bandVV, mask=bandVV,
# # ##                   connectivity=square(3))
# # ##    bandVV = result
# # #



# # #data=concatenate((normal(1,.2,5000),normal(2,.2,2500)))
# # #y,x,_=hist(data,100,alpha=.3,label='data')
# # #
# # #x=(x[1:]+x[:-1])/2 # for len(x)==len(y)
# # #
# # #
# # #expected=(1,.2,250,2,.2,125)
# # #params,cov=curve_fit(bimodal,x,y,expected)
# # #sigma=sqrt(diag(cov))
# # #plot(x,bimodal(x,*params),color='red',lw=3,label='model')
# # #legend()
# # #plt.show()
# # #new = pd.DataFrame(data={'params':params,'sigma':sigma},index=bimodal.__code__.co_varnames[1:])
# # #
# # #print(new)
    statsV = []
    return statsV


if __name__ == "__main__":

    ##### Sentinel S1A /S1B 
    path = "..."
    pathMapas = "..."

    arr = os.listdir(path)
    ### ordeno la lista
    arr.sort()
    print(arr)

    # Fit GMM
    #gmm = GaussianMixture(n_components = 3)
    #gmm = gmm.fit(hist)

    for i in arr:
    #    S1A
        # i = "20150427.data"
        # i = "20150109.data"
        # i = "20150521.data"
        # i = "20150403.data"
        # i = "20160207.data" 
        # i = "20160326.data"
        # i = "20160419.data"
    #    S1B
    #    i = "20161010.data"
    #    plt.clf()
        print(i)
        
    #    ax.cla()
        path2 = path + i
        fileVV = path2 +"/Sigma0_VV_db.img"
        statsVector = multimodal_analysis(fileVV)


