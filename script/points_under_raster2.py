import pandas as pd
import rasterio

#could not process lama lama guanico (row 79)
file_dir=r'C:/Users/M-RAM/Documents/InternshipNaturalis/trait-geo-diverse-ungulates-master'

#access file with list of taxa names
taxa2=pd.read_csv(file_dir+"/data/filtered/taxa.txt",header=None)
taxa2.columns=["taxon"]
taxa2=taxa2[35:80]
species_occ_dict2={}

#for i in taxa2["taxon"]:
 #   taxon_data = pd.read_csv(file_dir+"/data/filtered/%s.csv"%i)
  #  taxon_data["occurrence"] = 1 #add new variable with occurrence label (0/1)
    #add species dataframe to dict
   # species_occ_dict2["%s"%i] = taxon_data
    #check whether all species have been included and inspect dictionary
#if len(species_occ_dict2.keys())==len(taxa2["taxon"]):
 #   print("All species dataframes now in dictionary")
#else:
 #   print("Error: not all species dataframe included")
#print(species_occ_dict2)

#for key in species_occ_dict2:
for i in taxa2["taxon"]:
    data = pd.read_csv(file_dir+"/species_occ/%s_occ_dataframe.csv"%i)
    spec = data["taxon_name"][0]
    spec = spec.replace(" ","_")
    print(spec)
    src = rasterio.open(file_dir + "/data/GIS/%s_raster_clip.tif" % spec)

     # extract longitude and latitude and store them in normal list (as opposed to pandas Series)
    lon = data["decimal_longitude"]
    lat = data["decimal_latitude"]
    lat = pd.Series.tolist(lat)
    lon = pd.Series.tolist(lon)
    print("processing species %s" % spec)
    # go through bands iteratively
    for i in range(1, 42):
        array = src.read(i)
        band_name = "band %s" % i
        data[band_name] = None
        print("processing band %s" % i)
        for j in range(0, len(data)):
                # What is the corresponding row and column in our image?
            row, col = src.index(lon[j], lat[j])  # spatial --> image coordinates
                # print(f'row,col=\t\t({row},{col})')
                # What is the value?
            value = array[row, col]
            data[band_name][j] = value
    data.to_csv(file_dir + "/species_occ_env/%s_env_dataframe.csv" % spec)
