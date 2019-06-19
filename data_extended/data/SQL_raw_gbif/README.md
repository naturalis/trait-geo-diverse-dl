- All files in this folder were created based on a relational database .db file containing all GBIF occurrences for all ungulate species.
- To reproduce the creation of these files, the .db file can be downloaded from the following link: https://www.dropbox.com/s/rlucc0flms7gbkc/tgd.db?dl=0
- To open this file it is recommended to use [SQLiteStudio](https://sqlitestudio.pl/index.rvt). Once installed, the database can be opened using the Database -> add a database option.
- To export a csv file with occurrences for all species open the occurrences table and set the tab in the view screen to data (see image below) and click the export table option.
- Name the file "occurrences_all_species.csv" and make sure to export it twice to the correct folders in your local github clone ("../trait-geo-diverse/data_extended/data/SQL_raw_gbif) and 
("../trait-geo-diverse/data_GIS_extended/data/SQL_raw_gbif).

![](images/export_database.PNG)

