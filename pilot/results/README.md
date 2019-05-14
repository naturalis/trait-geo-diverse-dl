Pilot results
===========

The global performance metrics of the pilot DNN model can be found in the [\_DNN_performance](\_DNN_performance) folder. Next to this there is a separate folder for each species. These folders contains two categories of files. The first category pertains to the species-specific DNN model parameters and weight files for reproducibility and evaluation. These are contained in the .h5, model.json and feature_impact.png files. Next to this, each species folder contains a map with the filtered occurrences from GBIF, a Geotiff with predicted distributions and a resized color map for enhanced visualization. 

If we take the [Impala](Aepyceros_melampus) as an example, we can see that its known occurrences are located in South-Eastern Africa (top-left image). In the top-right image, we can see that aggregated over all samples, the three variables in the DNN model with the highest impacts on the predicted probability of presence were pHCaCl (Soil pH), Mean temperature of the Wettest Quarter and PETSeasonality (monthly variability in evapotranspiration). Each dot represents a single sample from our test dataset and the impact of the feature value on final predicted probability for each particular sample is calculated using Shapley values. For an explanation of Shapley values, see: https://christophm.github.io/interpretable-ml-book/shapley.html.

The model level insight this provides us with is that in the case of the Impala we can see that a high pH value will have a positive impact on the predicted probability of occurrence, whereas high seasonality  and high temperature in the wettest quarter have a negative impact on predicted probability of occurrence. The final world-wide predicted distribution of the species by the model can be seen in the bottom image.


Known occurrences          |  Variable importance and impact  |
:-------------------------:|:-------------------------:
<img src="Aepyceros_melampus/Aepyceros_melampus_occurrence_map.png" alt="drawing" width="400"/>  |  <img src="Aepyceros_melampus/Aepyceros_melampus_feature_impact.png" alt="drawing" width="500"/> |

And the resulting map    |    
:-------------------------:
<img src="Aepyceros_melampus/Aepyceros_melampus_predicted_map_color.png" alt="drawing"/> |



