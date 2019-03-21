# Floods-monitoring-with-SAR

The detection of flooded areas in SAR satellite images is carried out. A multimodal function is adjusted to the histogram of each SAR image and statistics are obtained that allow the discrimination of the zones.


Satellite Data:
 - Sentinel-1. SAR in C-Band C.  Interferometric Wide (IW) swath mode. VV polarisation. 



En la figura se presenta, el histograma de las imagenes satelitales (izquierda) junto a la función multimodal ajustada (con sus máximos) y la imagen satelital(derecha) en la cual se encuentran segmentados los cuerpos de agua utilizando información del histograma. 

<p align="center">
  <img width=850 src="Histogram_and_water.gif"/>
 </p>




Dependences: 

    python - Numpy
    python - Gdal
    python - Peakutils
    python - Matplotlib
    python - Scipy
    python - Imageio
