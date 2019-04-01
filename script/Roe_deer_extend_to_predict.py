import pandas as pd
import rasterio

file_dir=r'C:/Users/M-RAM/PycharmProjects/InternshipNaturalis/github_trait_geo_diverse_dl/trait-geo-diverse-dl'

#read in data
data = pd.read_csv(file_dir + "/data/capriolus_trial/Capriolus_capriolus_location_to_predict_env.csv")

spec = data["taxon_name"][0]
spec = spec.replace(" ","_")
# extract longitude and latitude and store them in normal list (as opposed to pandas Series)
lon = data["decimal_longitude"]
lat = data["decimal_latitude"]
lat = pd.Series.tolist(lat)
lon = pd.Series.tolist(lon)
#print("processing species %s" % spec)

#read in raster
src = rasterio.open(r'C:/Users/M-RAM/PycharmProjects/InternshipNaturalis/trait-geo-diverse-dl/data/GIS/spec_stacked_raster_clip/%s_raster_clip.tif'%spec)

# go through bands iteratively
for i in range(1, 42): ##RERUN TONIGHT......(GOT 31 Bands finished in 3 hours.....)
    array = src.read(i)
    band_name = "band %s" % i
    data[band_name] = None
    print("processing band %s" % i)
    for j in range(0, len(data)):
        #print("processing observation %s"%j)
        # What is the corresponding row and column in our image?
        row, col = src.index(lon[j], lat[j])  # spatial --> image coordinates
        # print(f'row,col=\t\t({row},{col})')
        # What is the value?
        value = array[row, col]
        data[band_name][j] = value
    data.to_csv(file_dir + "/data/capriolus_trial/Capriolus_capriolus_location_to_predict_env.csv")
data.to_csv(file_dir + "/data/capriolus_trial/Capriolus_capriolus_location_to_predict_env.csv")