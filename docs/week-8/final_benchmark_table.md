# **Week 8 – Reproducibility & Modular Project Design**
## **Benchmark Table** <br>
Name: Rhys Brown <br><br>



**Table 1: Benchmark Table comparing the performance of eight (8) Classifier Machine Learning Models on Triage Dataset**
|Model|Accuracy|Recall ESI 1|Macro F1|Training Time|Inference Time|Explainability|
|---|---|---|---|---|---|---|
|Dummy Classifier|0\.38|0\.0|0\.2|6\.35 ms|1\.12 ms|**N/A.** All results are generated randomly\.|
|Decision Tree|0\.58|0\.0|0\.27|1\.32 s|3\.66 ms|**High.** A decision chain for each inference can be generated\.|
|Base Logistic Regression|0\.67|0\.25|0\.49|18\.71 s|0\.55 ms|**High.** The coefficient relating each feature to an increase in ESI can be found\.|
| Tuned Logistic Regression Model* | 0.69 | 0.25 | 0.50 | 2.87 mins | 0.16 ms | The coefficient relating each feature to an increase in ESI can be found\.|
|Random Forest* |0\.59|0\.25|0\.46|26\.40 mins|52\.41 ms|**Medium.** Model is harder to interpret than decision tree\.|
|Gradient Boosting|0\.57|0\.38|0\.43|24\.72 mins|4\.73 ms|**Medium.** Model is harder to interpret than decision tree and random forest\.|
|Multi-Layer Perceptron|0\.67|0\.31|0\.46|6\.93 mins|3\.22 ms|**Low.** Neural Networks are notoriously difficult for humans to interpret\.|
| **Ensemble Model** | 0.67 | 0.31 | 0.54 | 3.05 mins | 19.18 ms | **Medium.** Model is comprised of Logistic Regression and Random_Forest. Two readily explainable models |

> [!NOTE]
> Ensemble Model is the winning model. It is comprised of the models with an asterisk next to them.