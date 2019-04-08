# Floods-monitoring-with-SAR

The detection of flooded areas in SAR satellite images is carried out. A multimodal function is adjusted to the histogram of each SAR image and statistics are obtained that allow the discrimination of the zones.


Satellite Data:
 - Sentinel-1. SAR in C-Band.  Interferometric Wide (IW) swath mode. VV polarisation. 


Description:

The figure shows the histogram of the satellite images (left) together with the adjusted multimodal function (with its maximums) and the satellite image (right) in which the bodies of water are segmented using information from the histogram.

<p align="center">
  <img width=850 src="Histogram_and_water.gif"/>
 </p>

<p align="center">
  <img width=850 src="Histogram_evolution.gif"/>
 </p>



Dependences: 

    python - Numpy
    python - Gdal
    python - Peakutils
    python - Matplotlib
    python - Scipy
    python - Imageio
