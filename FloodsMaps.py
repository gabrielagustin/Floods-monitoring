# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
Created on Thu Jun 28 14:46:41 2018

@author: gag

Script that obtains maps of flooded areas
Thresholding is applied using the values obtained from the
adjusting the multimodal function to the histogram (average
and deviation statistics of each Gaussian)

"""

from matplotlib import cm


def flood_maps(bandVV, statsV):
    mu1 = statsV[0]
    sigma1 = statsV[1]
    mu2 = statsV[2]
    sigma2 = statsV[3]
    mu3 = statsV[4]
    sigma3 = statsV[5]
    ### for ciudad
    thresholdedCity = deepcopy(bandVV)
    thresholdedCity[thresholdedCity < -5] = 0
    thresholdedCity[thresholdedCity > 5] = 0   
#    thresholdedCity[thresholdedCity != 0] = 1
    
    ### for water
    thresholdedW = deepcopy(bandVV)
    thresholdedW[thresholdedW > mu1 + sigma1] = 0
    thresholdedW[thresholdedW < mu1 - sigma1] = 0 
#    thresholdedW[thresholdedW != 0] = 1
    
    ### for vegetated areas
    thresholdedV = deepcopy(bandVV)
    thresholdedV[thresholdedV > mu3 + sigma3] = 0
    thresholdedV[thresholdedV < mu3 - sigma3] = 0
#    thresholdedV[thresholdedV != 0] = 1
        
    # for third max
    thresholdedNew = deepcopy(bandVV)
    thresholdedNew[thresholdedNew > mu2 + sigma2] = 0
    thresholdedNew[thresholdedNew < mu2 - sigma2] = 0   
#
#    ######--------------------------------------------------------------------- 
#    ###### se plotean los mapas de inundacion con tres clases
#    ##### Vegetacion-Agua-Tercer clase
##  for x in range(subwin_size, w-subwin_size,subwin_size):
##    for y in range(subwin_size, h-subwin_size,subwin_size):    
##        print(y-subwin_size)
##        print(y+subwin_size)
##        print(x-subwin_size)
##        print(x+subwin_size)
###        iy = y-subwin_size
###        jy = y+subwin_size
###        ix = x-subwin_size
###        jx = x+subwin_size
##        subwin = bandVV[x-subwin_size:x+subwin_size, y-subwin_size:y+subwin_size]
###        hist = genHist(subwin)         # Generate histogram
##        fig, ax = plt.subplots()
##        plt.imshow(subwin)
##        lcNew = subwin.flatten('C')
##        fig, ax = plt.subplots()
##        yy, xx, _= plt.hist(lcNew,500, [-30,-1], facecolor='gray', normed=1) 
####        plt.xlim(-30, -1)
####        plt.ylim(0, 0.3)
##        plt.show()
###        
###        plt.pause(5)
#   
#    ### se aplican los centroide y los desvios de la funcion multimodal encontrada
#    ### para clasificar la imagen satelital
#    #### la primer guasiana representa agua libre
#   
#    coeff = 2.5   
#   
#    r1 =(mu1-sigma1*coeff)
##    print(r1)
#    r2 = (mu1+sigma1*coeff)
##    print(r2)
#    print("Agua:"+str([r1,r2]))
#    #### la gausiana intermedia representa la transicion entre agua y suelo vegetado
#    im0 = ax.imshow(bandVV, extent=[xmin,xmax,ymin,ymax], cmap=my_cmap2, vmin=r1, vmax=r2, interpolation="Bilinear")
#    r3 = (mu2-sigma2*coeff)
##    print(r3)
#    r4 = (mu2+sigma2*coeff)
##    print(r4)  
#    print("Transicion:"+str([r3,r4]))
#    im1 = ax.imshow(bandVV, extent=[xmin,xmax,ymin,ymax], cmap=my_cmap5, vmin=r3, vmax=r4, interpolation="Bilinear")
#    ### la tercer gausiana representa suelo/vegetacion
#    r5 = (mu3-sigma3*coeff)
##    print(r5)
#    r6 = (mu3+sigma3*coeff)
##    print(r6)  
#    print("Vegetacion/suelo:"+str([r5,r6]))
#    im2 = ax.imshow(bandVV, extent=[xmin,xmax,ymin,ymax], cmap=my_cmap3, vmin=r5, vmax=r6, interpolation="Bilinear")
#    ### se identifican ciudades
#    r7 = -6
#    r8 = 5
#    print("Ciudades:"+str([r7,r8]))
#    im3 = ax.imshow(bandVV, extent=[xmin,xmax,ymin,ymax], cmap=my_cmap1, vmin=r7, vmax=r8, interpolation="Bilinear")
#    # Build the colorbar on the right
#    # Place a colorbar next to the map
#    cbar = fig.colorbar(im0, ticks=[-1, 0, 1], orientation='horizontal')
#    cbar = fig.colorbar(im1, ticks=[-1, 0, 1], orientation='horizontal')
##    cbar = im0.colorbar(im0, 'right', size='5%', pad='5%')
#    # Build the colorbar on the bottom
#    # cbar = m.colorbar(im, 'bottom', size='5%', pad='8%')
##    cbar.set_label('Degrees C')
# 
##------------------------------------------------------------------------------  
#     

    ### colors maps
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


    
#    r1 = int(np.round(mu1-sigma1))
#    print(r1)
#    r2 = int(np.round(mu1+sigma1))
#    print(r2)
    img0 = ax.imshow(bandVV,extent=[xmin,xmax,ymin,ymax], cmap=my_cmap1, interpolation="Bilinear")
#    rango = list(range(r1, r2, 2))
#    print(rango)    
##    ax.contourf(bandVV, cmap=my_cmap2, levels = rango)
#    r3 = int(np.round(mu2-sigma2))
#    print(r3)
#    r4 = int(np.round(mu2+sigma2))
#    print(r4)  
#   
#    rango = list(range(r3, r4, 2))
#    print(rango)
#    ax.contourf(bandVV, cmap=my_cmap3, levels = rango)
#    r5 = int(np.round(mu3-sigma3))
#    print(r5)
#    r6 = int(np.round(mu3+sigma3))
#    print(r6)  
#    
#    rango = list(range(r5, r6, 1))
#    print(rango)
#    ax.contourf(bandVV, cmap=my_cmap1, levels = rango)    
#    
    
    img1 = ax.imshow(thresholdedV,extent=[xmin,xmax,ymin,ymax], cmap=my_cmap3, interpolation="Bilinear")

    water = np.ma.masked_where(thresholdedV != 0, thresholdedW) 
    img2 = ax.imshow(water,extent=[xmin,xmax,ymin,ymax], cmap=my_cmap2, interpolation="Bilinear")
    
    thresholdedV = deepcopy(bandVV)
#    thresholdedCity[thresholdedCity != 0] = 1
#    img3 = ax.imshow(thresholdedCity,extent=[xmin,xmax,ymin,ymax], cmap=my_cmap4, interpolation="Bilinear")
    city = np.ma.masked_where(water!= 0, thresholdedCity)        
    img3 = ax.imshow(city,extent=[xmin,xmax,ymin,ymax], cmap=my_cmap4, interpolation="Bilinear")

    New = np.ma.masked_where(city != 0, thresholdedNew)
    thresholdedNew[thresholdedNew != 0] = 1
    img4 = ax.imshow(New,extent=[xmin,xmax,ymin,ymax], cmap=my_cmap1, interpolation="Bilinear")
    
    ax.yaxis.set_major_locator(plt.MaxNLocator(5))
    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax.xaxis.tick_top()
#    plt.savefig(str(pathMapas) + str(fecha) +'.png')
#    plt.pause(3)
#--------------------------------------------------------------------------
    plt.show()

