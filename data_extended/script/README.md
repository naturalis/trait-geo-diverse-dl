The scripts were used in the following order:

1. [GBIF records](1.Filter_GBIF_records_from_SQL_database.ipynb) were filtered. 
2. [Species occurrence maps](2.Create_occurrence_maps.ipynb) were created. 
2. Species and global [prediction dataframes](3.Create_species_and_global_prediction_dataframes.ipynb) were generated.
4. A DNN was [trained](4.Train_DNN.ipynb) to predict the probability of species occurrence for the training set of presence \& pseudo-absences.
5. The trained DNN was used to [predict the species potential global](5.Global_predictions_trained_DNN.ipynb) distribution. 
