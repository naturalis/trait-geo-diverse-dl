The scripts were used in the following order:

1. [Species occurrence maps](1.Create_occurrence_maps) were created. 
2. The environmental variable rasters were [stacked](2.Stacking_environmental_rasters).
2. [Species and global prediction dataframes](3.Create_species_and_global_prediction_dataframes) were generated.
4. A DNN was [trained](4.Train_DNN) to predict the probability of species occurrence for the training set of presence \& pseudo-absences.
5. The trained DNN was used to [predict the species potential global](6.Global_predictions_trained_DNN) distribution. 
