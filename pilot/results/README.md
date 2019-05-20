# Pilot results

The results of the pilot study are subdivided into two parts. The [DNN performance](_DNN_performance) folder lists the aggregate model performance in terms of test loss, accuracy, AUC and confidence band width over all species.
Next to this, there are separate folders per species. These folders contain the species specific model structure and weights in the .h5 and .json files for reproducibility. Additionally, the model output is provided with 
1) a graph listing variable importance based on shapley values* 2) A map with filtered occurrence records from GBIF 3) A GeoTiff containing predicted distribution in grayscale 4) A recolored map containing the predicted distribution.
*(for an explanation of shapley values see: https://christophm.github.io/interpretable-ml-book/shapley.html)


If we take [Aepyceros melampus](Aepyceros_melampus) as an example, we can see in the top-left figure that it's occurrence records are all from South-Eastern Africa. The top-right figure shows the variables the model learned to assign
most weight to during training, with each dot representing a single sample. Aggregated over all samples, the three variables with the hightest impact are the pH, Mean temperature of wettest quarter and Seasonality of potential evapotranspiration. 
Looking at the figure we see that if pH is high, this has a positive impact of up to 0.4 on model output, whereas the opposite goes for mean temperature of the wettest quarter and seasonalit of potential evapotranspiration. The final
model predictions over the entire globe this results in are provided in the bottom figure.

| Species occurrence             |  Variable importance |
:-------------------------:|:-------------------------:
<img src="https://github.com/naturalis/trait-geo-diverse-dl/blob/master/pilot/results/Aepyceros_melampus/Aepyceros_melampus_occurrence_map.png" alt="drawing" width="400"/> |<img src="https://github.com/naturalis/trait-geo-diverse-dl/blob/master/pilot/results/Aepyceros_melampus/Aepyceros_melampus_feature_impact.png" alt="drawing" width="400"/>
| Predicted distribution            |
:-------------------------:
<img src="https://github.com/naturalis/trait-geo-diverse-dl/blob/master/pilot/results/Aepyceros_melampus/Aepyceros_melampus_predicted_map_color.png" alt="drawing" width="800"/> 