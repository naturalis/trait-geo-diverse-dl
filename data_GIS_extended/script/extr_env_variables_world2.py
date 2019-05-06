from shapely.geometry import Point
import matplotlib.pyplot as plt
from rasterio.mask import mask
from rasterio.plot import show
from rasterio.plot import plotting_extent
from rasterio.warp import reproject, Resampling
from natsort import natsorted
import earthpy.spatial as es
import gdal
from osgeo import osr,gdal_array
import xarray as xr
import netCDF4
import pandas as pd
import numpy as np
import geopandas
import rasterio
import pycrs
import os

file_dir=r'C:/Users/Mark.Rademaker/PycharmProjects/InternshipNaturalis/venv/github_trait_geo_diverse_dl/trait-geo-diverse-dl/extended model extra observations and variables'

#create list of raster file locations and a list containing only the names of each raster
list_bioclim_files=[]
names_bioclim=[]

for root, dirs, files in os.walk(file_dir+"/data/GIS/wc5"):
    for file in files:
        if file.endswith('.tif') and "stacked" not in file:
            list_bioclim_files.append(file_dir+"/data/GIS/wc5/"+file)
            name=file.replace(".tif","")
            names_bioclim.append(name)
            names_bioclim=natsorted(names_bioclim,key=lambda y: y.lower())


#create list of raster file locations and a list containing only the names of each raster
list_envirem_files=[]
names_envirem=[]

for root, dirs, files in os.walk(file_dir+"/data/GIS/5_deg"):
    for file in files:
        if file.endswith('.tif') and "stacked" not in file:
            list_envirem_files.append(file_dir+"/data/GIS/5_deg/"+file)
            name=file.replace(".tif","")
            names_envirem.append(name)
            names_envirem=natsorted(names_envirem,key=lambda y: y.lower())

list_historic_files=[]
names_historic=[]

##stack the rasters
for root, dirs, files in os.walk(file_dir+"/data/GIS/historic_1_deg"):
    for file in files:
        if file.endswith('.tif') and "time" not in file and "stacked" not in file:
            list_historic_files.append(file_dir+"/data/GIS/historic_1_deg/"+file)
            name=file.replace(".tif","")
            names_historic.append(name)

#create list of raster file locations and a list containing only the names of each raster
list_species_files=[]
names_species=[]

for root, dirs, files in os.walk(file_dir+"/data/GIS/spec_presence"):
    for file in files:
        if file.endswith('.tif') and "stacked" not in file:
            list_species_files.append(file_dir+"/data/GIS/spec_presence/"+file)
            name=file.replace(".tif","")
            names_species.append(name)

# Stack ENVIREM+BIOCLIM+HISTORIC+SPECIES dataset
list_variables = []
list_names = []
for item in list_bioclim_files:
    list_variables.append(item)
for item in list_envirem_files:
    list_variables.append(item)
for item in list_historic_files:
    list_variables.append(item)
for item in list_species_files:
    list_variables.append(item)

#es.stack(list_variables, file_dir + "/data/GIS/env_stacked/stacked_env_variables.tif")

for item in names_bioclim:
    list_names.append(item)
for item in names_envirem:
    list_names.append(item)
for item in names_historic:
    list_names.append(item)
for item in names_species:
    list_names.append(item)

###extract raster values at world locations to predict
data=pd.read_csv(file_dir + "/data/GIS/world_locations_to_predict.csv")
src = rasterio.open(file_dir+'/data/GIS/env_stacked/stacked_env_variables.tif')

lon = data["decimal_longitude"]
lat = data["decimal_latitude"]
lat = pd.Series.tolist(lat)
lon = pd.Series.tolist(lon)

for i in range(34, 68):
    array = src.read(i)
    band_name = list_names[i]
    data[band_name] = None
    print("processing band %s" % i)
    for j in range(0, len(data)):
        # What is the corresponding row and column in our image?
        row, col = src.index(lon[j], lat[j])  # spatial --> image coordinates
        # print(f'row,col=\t\t({row},{col})')
        # What is the value?
        value = array[row, col]
        data[band_name][j] = value
data.to_csv(file_dir + "/data/GIS/world_env_dataframe2.csv")


