import pandas as pd
import rasterio

file_dir=r'C:/Users/Mark.Rademaker/PycharmProjects/InternshipNaturalis/venv/github_trait_geo_diverse_dl/trait-geo-diverse-dl/concept proof'

#access file with list of taxa names
taxa=pd.read_csv(file_dir+"/data/spec_filtered/taxa.txt",header=None)
taxa.columns=["taxon"]

species_occ_dict={}

for i in taxa["taxon"]:
    taxon_data = pd.read_csv(file_dir+"/data/spec_filtered/%s.csv"%i)
    #add species dataframe to dict
    species_occ_dict["%s"%i] = taxon_data
    #check whether all species have been included and inspect dictionary
if len(species_occ_dict.keys())==len(taxa["taxon"]):
    print("All species dataframes now in dictionary")
else:
    print("Error: not all species dataframe included")

##Subset the dataframe into four parts
# access file with list of taxa names
taxa = pd.read_csv(file_dir + "/data/spec_filtered/taxa.txt", header=None)
taxa.columns = ["taxon"]
taxa1 = taxa[0:35]
taxa2 = taxa[35:80]
taxa3 = taxa[80:120]
taxa4 = taxa[120:154]

#Loop4
for i in taxa4["taxon"]:
    data = pd.read_csv(file_dir+"/data/spec_occ/%s_occ_dataframe.csv"%i)
    spec = data["taxon_name"][0]
    spec = spec.replace(" ","_")
    src = rasterio.open(file_dir+'/data/GIS/spec_stacked_raster_clip/%s_raster_clip.tif'%spec)

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
    data.to_csv(file_dir + "/data/spec_occ_env/%s_env_dataframe.csv" % spec)