The scripts were used in the following order:

1. The environmental variable rasters were [stacked](Stacking_environmental_rasters).
2. [Species and global prediction dataframes](Create_species_and_global_prediction_dataframes) were generated.
3. [Species occurrence maps](Create_occurrence_maps) were created.
4. A DNN was [trained](Train_DNN) to predict the probability of species occurrence for the training set of presence \& pseudo-absences.
5. The trained DNN was used to [predict the species potential global](Global_predictions_trained_DNN) distribution. 
