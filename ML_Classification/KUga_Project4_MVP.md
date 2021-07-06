## Detecting Wear on a Computer Numerically Controlled Mill Tool

Kalu Chibueze Uga

#### Abstract
Advanced manufacturing and large scale production depend highly on Computer Numerically Controlled (CNC) machining. However, many companies are not efficient because they have a poor approach to mill tool failure management. Mill tool wear can lead to end products that will fail final Quality Check, waste of raw material, waste of coolant materials, and can result in unnecessary financial expenses if the mill tool breaks. The goal of this project is to predict wear on a CNC milling tool so that the milling tool can be replaced before products are ruined due to poor cutting structure of the worn mill tool.

#### Data 
The data will be Milling Data Set from https://www.kaggle.com/shasun/tool-wear-detection-in-cnc-mill that was provided by UNIVERSITY OF MICHIGAN SMART LAB. The dataset consists of a time series experiment from 18 CNC machines for variations of tool condition, feed rate, and clamp pressure with a sampling rate of 100 ms. The output of each experiment shows tool condition (worn or unworn), finalized machining (yes/no), and visual inspection (yes/no).

#### Exploratory Data Analysis
The distribution of the classes in the dataset, seen in Figure 1a, shows that the classes are within 10% of the expected mean of the total classes. Thus, we can say that the dataset is fairly balanced. Also, only observations from actual machining operations will be used for analysis. Figure 1b shows the count of all actual maching operations.
| a, Percentage of classes in dataset | b, Count of machining operations |
|:----: |:------:|
| <img src="/Users/amyphillip/Desktop/Metis/project_4_ml_classification/ML_classification/plots/class_percent.png" width = "450" height = "300">   | <img src="/Users/amyphillip/Desktop/Metis/project_4_ml_classification/ML_classification/plots/machining_process.png" width = "450" height = "300">    |
Figure 1, EDA

#### Metrix
The classification matrix that will be used for the fairly balanced dataset are;
* Accuracy
* AUC - Probability that the classifier assigns the high score to the worn class.
* Confusion Matrix

The goal is to try and predict all the worn mill tools correctly.  Threshold can be adjusted (lower) to account for more false negatives (high recall). It is imperative to identify all worn tools because ta won tool can break and result in more financial loss associated with milling machine repairs, loss of expensive mill tool, non-productive time from hault in operations, and loss of future contracts. Thus, saying that a mill tool is worn, but the prediction is wrong, has less harm than saying that the mill tool is unworn.

A plot of model comparison and the XGBOOST class plot is shown below.
| 2a, Model Comparison | 2b, XGBOOST Class Comprison |
|:----: |:------:|
| <img src="/Users/amyphillip/Desktop/Metis/project_4_ml_classification/ML_classification/plots/Model_Comparison.png" width = "450" height = "300">   | <img src="/Users/amyphillip/Desktop/Metis/project_4_ml_classification/ML_classification/plots/actual_predicted.png" width = "450" height = "300">    |
Figure 2,

