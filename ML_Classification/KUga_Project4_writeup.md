## Detecting Wear on a Computer Numerically Controlled Mill Tool

Kalu Chibueze Uga

#### Abstract
Advanced manufacturing and large scale production depend highly on Computer Numerically Controlled (CNC) machining. However, many companies are not efficient because they have a poor approach to mill tool failure management. Mill tool wear can lead to end products that will fail final Quality Check, waste of raw materials, waste of coolant materials, and can result in unnecessary financial expenses if the mill tool breaks. The goal of this project is to predict wear on a CNC milling tool so that the milling tool can be replaced before products are ruined due to poor cutting structure of the worn mill tool.

#### Design
* False negatives have greater negative financial impact than false positives, therefore we plan to penalize false negatives more in order to improve recall. 
* Seek a model with strong predictive ability knowing that interpretability will be compromised. 
* Correctly predicting majority of worn mill tools will reduce negative financial impact associated with milling machine repairs, loss of expensive mill tool, non-productive time from hault in operations, and loss of future contracts. 
* It is assumed that observations where there is no cutting activity does not have any impact on mill tool wear

#### Data 
The data is Milling Data Set from https://www.kaggle.com/shasun/tool-wear-detection-in-cnc-mill that was provided by UNIVERSITY OF MICHIGAN SMART LAB. The dataset consists of a time series experiment from 18 CNC machines for variations of tool condition, feed rate, and clamp pressure with a sampling rate of 100 ms. The output of each experiment shows tool condition (worn or unworn), finalized machining (yes/no), and visual inspection (yes/no).

#### Algorithm
*Exploratory Data Analysis*

1. Pandas and numpy were used for data cleansing and manipulation.
2. Matplotlib and seaborn were used for data visualization.

The distribution of classes in the dataset, seen in Figure 1a, shows that the classes are within 10% of the expected mean of the total classes. Thus, we can say that the dataset is fairly balanced. Also, only observations from actual machining operations will be used for analysis. Figure 1b shows the count of all actual maching operations.
| a, Percentage of classes in dataset | b, Count of machining operations |
|:----: |:------:|
| <img src="/Users/amyphillip/Desktop/Metis/project_4_ml_classification/ML_classification/plots/class_percent.png" width = "450" height = "300">   | <img src="/Users/amyphillip/Desktop/Metis/project_4_ml_classification/ML_classification/plots/machining_process.png" width = "450" height = "300">    |
Figure 1, EDA

*Metrics and Model*

The classification matrix that will be used for the fairly balanced dataset are accuracy, AUC, f_beta, and Confusion Matrix. An initial model that used Logistic Regression and one feature (FEEDRATE) was used to get a benchmark to build upon. Feature Engineering was performed to check for improvement in the benchmark model.
Six classification models were tested on the dataset and the best predictive performer is Extreme Gradient Booster (XGBOOT) Classifier. The AUC plot for all models is shown in figure 2a, and the comparison of XGBOOT class prediction against the true class values is shown in figure 2b. XGBOOST accuracy was 99.42% with few misclassified observations. 

| 2a, AUC Comparison | 2b, XGBOOST Predicted Class |
|:----: |:------:|
| <img src="/Users/amyphillip/Desktop/Metis/project_4_ml_classification/ML_classification/plots/roc_auc_curve_comparison.png" width = "450" height = "300">   | <img src="/Users/amyphillip/Desktop/Metis/project_4_ml_classification/ML_classification/plots/actual_predicted.png" width = "450" height = "300">    |
Figure 2, XGBOOST Performance

Decreasing the threshold from 0.5 to 0.45 penalized the false negatives more. The result was a decrease in number of false negatives and an increase in recall from 0.9958 to 0.9972 as one would expect. The confusion matrix is shown in figure 3.

| 3a, threshold = 0.5 | 3b, threshold = 0.45 |
|:----: |:------:|
| <img src="/Users/amyphillip/Desktop/Metis/project_4_ml_classification/ML_classification/plots/xgboost_conf_matrix.png" width = "450" height = "300">   | <img src="/Users/amyphillip/Desktop/Metis/project_4_ml_classification/ML_classification/plots/xgboost_conf_matrix_2.png" width = "450" height = "300">    |
Figure 3, XGBOOST Confusion Matrix

#### Tools
1. Pandas and numpy were used for data cleansing and manipulation.
2. Matplotlib and seaborn were used for data visualization.
3. FLASK and plotly were used for application based data visualization

#### Communication
The findings from the project shows that accuracy and AUC are interpretable metrics for balanced datasets. Adjusting threshold lower to increase recall is more interpretable than f_beta score. Optimal threshold can be found at the threshold where recall and precision intercept on the recall, precision, and threshold curve. XGBOOST is an excellent choice because it has optimal predictive ability even though there is no interpretable measure on how the important features  influence the results produced. Some of the findings are presented via FLASK APP and Plotly plot as shown in figure 4..

| 4a, Flask App Home | 4b, AUC plot |
|:----: |:------:|
| <img src="/Users/amyphillip/Desktop/Metis/project_4_ml_classification/ML_classification/plots/flask_home.png" width = "450" height = "300">   | <img src="/Users/amyphillip/Desktop/Metis/project_4_ml_classification/ML_classification/plots/flask_2.png" width = "450" height = "300">    |
Figure 4, Screenshot of Flask App.

