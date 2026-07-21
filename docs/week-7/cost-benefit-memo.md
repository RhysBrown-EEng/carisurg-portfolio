# **Cost Benefit Memo For Machine Learning-Based Classifiers for Emergency Department Triage**

**Author** Rhys Brown <br>
**Dates:** 20/7/2026

## **Verdict**

> [!IMPORTANT]
> The **Random Forest** model is recommended for machine learning-based triage due to its low tendency to under-triage patients compared to the other models.

## **Recap**
### 1. Dataset:
The dataset contains the triage data associated with 55,121 emergency department encounters within the United States. It consisted of Emergency Severity Index (ESI) score along with 225 other features taken from each encounter. 200 chief complaint variables and 25 vitals exist in the dataset.


A major class imbalance exists between ESI level 1 and 5 cases, only making up roughly **0.13%** and **2%** of the total cases respectively, leaving little data for the models to learn on. 

### 2. Method:
A dummy classifier, decision tree and logistic regression model were trained on triage data with the goal of accurately predicting a acuity score. 

Furthermore, features were mathematically-derived based on the vitals in order to train and Random Forest, Gradient Boosting and Multi-Layer Perceptron Model.

Six (6) models in total were trained on the dataset and compared against one another:
- **Dummy Classifier:** a classifier that select output classes based on simple rules, not based on patterns found in the data. It is used as a baseline to compare against the previous models.
- **Decision Trees:** A machine learning algorithm that classifies data by a series of yes/no decisions. The depth of the model refers to number of decisions from the first decision to the final output. Maximum depth of 10 was chosen to ensure the model was large enough whilst also not becoming too complex, learning from noise as opposed to genuine patterns.
- **Logistic Regression:** a machine learning classifier that predicts the likelihood of a given class which is then mapped to a class based on whether it is above or below a threshold. '
- **Random Forest:** a combination of decision trees that vote on the most likely class.
- **Gradient Boosting:** an algorithm that incrementally improves a decision treee.
- **Multi-layer Perceptron**: a small neural network made of perceptrons, a unit that combines linear combinations of previous results and a special math function to get an output.


## **Benchmark Table**
<br>

**Table 1: Benchmark Table comparing the performance of six (6) Classifier Machine Learning Models on Triage Dataset**
|Model|Accuracy|Recall ESI 1|Macro F1|Training Time|Inference Time|Explainability|
|---|---|---|---|---|---|---|
|Dummy Classifier|0\.38|0\.0|0\.2|4\.71 ms|0\.77 ms|N/A\. All results are generated randomly\.|
|Decision Tree|0\.58|0\.0|0\.27|534\.48 ms|1\.92 ms|High\. A decision chain for each inference can be generated\.|
|Logistic Regression|0\.67|0\.25|0\.49|9\.84 s|0\.17 ms|High\. The coefficient relating each feature to an increase in ESI can be found\.|
|Random Forest|0\.59|0\.25|0\.46|26\.40 mins|18\.97 ms|Medium\. Model is harder to interpret than decision tree\.|
|Gradient Boosting|0\.57|0\.38|0\.43|24\.72 mins|7\.04 ms|Medium\. Model is harder to interpret than decision tree and random forest\.|
|Multi-Layer Perceptron|0\.6|0\.31|0\.45|8\.27 mins|1\.23 ms|Low\. Neural Networks are notoriously difficult for humans to interpret\.|
<br>

> [!NOTE]
> Accuracy, Recall, F1-Score are measures of model performance:
> - Accuracy: the fraction of predictions made by the model that were correct.
> - Recall: the fraction of accurately predicted positives out of all true positives (0 - all false negatives, while 1- no false negatives).
> - Precision: the fraction of predicted positives that were true positives for a given class. (0 - all false positives, while 1- no false positives).
> - F1-score: a fraction balancing recall and precision that shows the overall discrimination ability of the model.
>
> Each of the above metrics exist in the range of [0, 1].


## **Arguments supporting Verdict**
### 1. Low Rates of Under-triage for ESI 2-5 :

As seen in *Figure 1*, the Random Forest model has the highest number of class-wise true positives for all non-ESI 1 classes. This reduces the risk of false negatives for critical cases. In medicine, false negatives are especially dangerous as they lead to longer waiting times before receiving required treatment if it even is administered. Therefore, false negatives must be especially reduced.

![6 Model Classifier Confusion Matricies](../week-7/figs/cm_classifiers.png "Logistic Regression Confusion Matrix")

**Figure 1:** Figure showing the confusion matrix for six (6) classifier models on the dataset.

### 2. Low clinical need for machine learning-based assistance in ESI 1 cases:
As seen in the benchmark table, the Random Forest model is outperformed in terms of ESI 1 recall by the Gradient Boosting Classifier and the Multi-Layer Perceptron. However, it should be noted that based on conversations with medical professionals such as Dr. Loren De Freitas,  ESI 1 cases are typically so readily apparent that a model is not needed. <br> <br>
Furthermore, in the case of such urgent cases, the formal procedure required to enter data into the model to receive a prediction will likely prove too time-intensive, rendering high ESI 1 recall unnecessary.

### 3. Decent Explainability:
Random Forest models have high level of explainability compared to neural networks such as the Multi-layer Perceptrons. Random Forest models expose feature importance which is crucial in helping clinicians understand how the model made its decision. <br> <br>
This explainabiility is especially important for medical applications as physician are responsible for the decisions made. Therefore, they must understand how the AI arrived at its conclusion so they can second the opinion or override it.

## **Arguments against Verdict**

### 1. Lower Macro Accuracy and F1 score:
As seen in the benchmark table, the Logistic Regression and Multi-layer Perceptron models both outperformed the Random Forest in terms of accuracy. <br><br>
However, this weakness is mitigated by the fact that the rate of under-triage is lower in the Random Forest model. Reducing under-triage is the single most important objective in creating a model that is safe for emergency department triage; therefore, lower overall accuracy is acceptable. 

### 2. Long Inference Time
The Random Forest model had the highest inference time by far at **18.97** milliseconds. This puts it at 2.69 times the inference time of the next closest model, the gradient boosting classifier. This as due to the large number of decision trees used in the model. <br> <br>
That said, at less than one 50th of a second, the inference time is so small that it is **not the rate-limiting step** in a machine learning-based triage system. The true rate-limiting step would likely be the time taken during data-entry.

### 3. Long Training Time
It was also observed that the Random Forest model had the longest training time. This was due to the long time required to find optimal hyperparameters (the researcher-defined settings for a given model). <br> <br>
This is not a significant challenge as the training time was relatively short compared to the weeks that other machine learning algorithms take to train. Furthermore,  training is a one-time investment which would not need to be repeated after the model is deployed.

## **Risks & Recommendation**

The Random Forest model is superior fr our applications currently but it is not without risk. The overall generalizability of the model on a Caribbean dataset is not known as yet. Furthermore, the performance still has room for improvement. Finally, the model is only one part of a wider machine learning-based triage system. Therefore keen focus is required to ensure the devices and staff training do not become point of friction that limit overall system effectiveness. 

The final recommendation of this report is to porceed with the Random Forest model with caution. Moreover, said model should be further optimized to improve accuracy, recall and F1-score.