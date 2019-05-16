# GIS datasets 
## Climate 
Both the [Bioclim](http://worldclim.org/version2) dataset and the [ENVIREM](https://deepblue.lib.umich.edu/data/concern/data_sets/gt54kn05f) dataset are used as climatic variables. 
![](images/bioclim.PNG)
### Datasets Bioclim 
1. BIO1 Annual Mean Temperature
2. BIO2 Mean Diurnal Range (Mean of monthly (max temp - min temp))
3. BIO3 Isothermality (BIO2/BIO7) (* 100)
4. BIO4 Temperature Seasonality (standard deviation *100)
5. BIO5 Max Temperature of Warmest Month
6. BIO6 Min Temperature of Coldest Month
7. BIO7 Temperature Annual Range (BIO5-BIO6)
8. BIO8 Mean Temperature of Wettest Quarter
9. BIO9 Mean Temperature of Driest Quarter
10. BIO10 Mean Temperature of Warmest Quarter
11. BIO11 Mean Temperature of Coldest Quarter
12. BIO12 Annual Precipitation
13. BIO13 Precipitation of Wettest Month
14. BIO14 Precipitation of Driest Month
15. BIO15 Precipitation Seasonality (Coefficient of Variation)
16. BIO16 Precipitation of Wettest Quarter
17. BIO17 Precipitation of Driest Quarter
18. BIO18 Precipitation of Warmest Quarter
19. BIO19 Precipitation of Coldest Quarter

### Datasets ENVIREM 
1. annualPET Annual potential evapotranspiration
2. aridityIndexThornthwaite Thornthwaite aridity index
3. climaticMoistureIndex Metric of relative wetness and aridity
4. continentality Average temp. of warmest and coldest month
5. embergerQ Emberger’s pluviothermic quotient
6. growingDegDays0 Sum of months with temperatures greater than 0 degrees
7. growingDegDays5 Sum of months with temperatures greater than 5 degrees
8. maxTempColdestMonth Maximum temp. of the coldest month
9. minTempWarmestMonth Minimum temp. of the warmest month
10. monthCountByTemp10 Sum of months with temperatures greater than 10 degrees
11. PETColdestQuarter Mean monthly PET of coldest quarter
12. PETDriestQuarter Mean monthly PET of driest quarter
13. PETseasonality Monthly variability in potential evapotranspiration
14. PETWarmestQuarter Mean monthly PET of warmest quarter
15. PETWettestQuarter Mean monthly PET of wettest quarter
16. thermInd Compensated thermicity index

## Topography
Median elevation variables were extracted from the [Harmonized World Soil Database ](http://www.fao.org/soils-portal/soil-survey/soil-maps-and-databases/harmonized-world-soil-database-v12/en/) and have a spatial resolution of 30 arcseconds. The topographic wetness index and the terrain roughness index are extracted from the [ENVIREM](https://deepblue.lib.umich.edu/data/concern/data_sets/gt54kn05f) dataset and have a spatial resolution of 30 arcseconds. 
### Datasets 
1. Slope
2. Aspect
![](images/slope.PNG)
## Soil 
The soil characteristics are extracted from the [Land-Atmosphere Interaction Research Group](http://globalchange.bnu.edu.cn/research/soilw) with a spatial resolution of 5 arcminutes. 

1. Bulk density
2. Clay percentage
3. pH CaCL
4. Organic carbon 

![](images/ph.PNG)

#Stacked raster datasets
##env_stacked
The [env_stacked](env_stacked) folder contains the environmental variable rasters stacked into a single GeoTiff,
as well as a text file containing the variable descriptions for each of the 41 bands in the GeoTiff.

##stacked raster clips
A [clip](spec_stacked_raster_clip) was made of the GeoTiff for each species, based on its IUCN range.
This clipped raster was used to generate pseudo-absence locations from.