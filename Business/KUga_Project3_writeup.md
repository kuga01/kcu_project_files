## Predictive Maintenance of Simulated Aircraft Gas Turbine Engines

Kalu Chibueze Uga

#### Abstract
Mechanical failure is expected of all mechanical equipment and it could have severe consequences like termination of contract due to downtime accrued. The ability to correctly predict equipment failure will help companies improve utilization of equipment parts and avoid unnecessary downtime. Predictive maintenance via machine learning is designed to help predict the probability of failure so that maintenance can be scheduled in advance and carried out only when needed. The goal of this project is to show that using historic dataset, we can find failure patterns that could be used to predict failure in the future. 

#### Design
* Since the cost of catastrophic failure is high (fatality or red money in excess of $ 1M), the proposed business impact is to reduce the quaterly rate of engine failures.
* Impact hypothesis: Predicting engine failure will help reduce the rate of engine failures since maintenance will be scheduled as needed.
* The solution path is to build a model to predict when an engine will likely fail.
* Correctly predicting over 70 percent of failures will help the company maintain its current contract and boost its ability to secure future contracts with our clients. Clients are generally pleased to know that an equipment maintenance is scheduled before an expected failure rather than a reactive approach to repair a failed equipment.
* It is assumed that the sensor readings are highly reliable and there are no extreme natural disturbances like weather.

#### Data 
The dataset will be NASA TurboFan Engine data provided by NASA. The data consists of sensor readings of the operating conditions of one hundred simulated aircraft gas turbine engines. Three files were provided; a train set, a test set, and the Remaining Useful Life (RUL) of the test set. The engines in the train set were operating until they failed, whereas, the engines in the test set have not failed. The rows in the dataset represent data collected every cycle for every engine.The train and test sets consist of Engine ID, Cycle, three operation settings, and twenty three sensor readings as features. 

#### Algorithm
*Exploratory Data Analysis*

1. Google Sheets was used for data cleansing and manipulation.
2. Visualized some features to find trends - The test data showed that some sensor readings and operation mode were constant for all the engines. These constant features were droped. The features that showed relationship with RUL were retained. Figure 1 shows feature dependence on RUL.
| Constant feature | Varying feature |
|:----: |:------:|
| <img src="https://github.com/kuga01/kcu_project_files/blob/main/Business/plot/sensor1_engine1_train.png" width = "450" height = "300">   | <img src="https://github.com/kuga01/kcu_project_files/blob/main/Business/plot/sensor14_engine1_train.png" width = "450" height = "300">    |
Figure 1, Feature dependence on RUL.

A plot of the distribution of SENSOR 9 shows a normal distribution as seen in Figure 2a. Figure 2b shows the current cycle and RUL of the first 10 engines in the test set.
| 2a, Distribution of SENSOR 9 | 2b, Cycle and RUL of first 10 engines |
|:----: |:------:|
| <img src="https://github.com/kuga01/kcu_project_files/blob/main/Business/plot/dist_s9_test.png" width = "450" height = "300">   | <img src="https://github.com/kuga01/kcu_project_files/blob/main/Business/plot/cycle_rul.png" width = "450" height = "300">    |
Figure 2, Sensor distribution and cycle plots on test set.

#### Model
* Gradient Booster Classifiers will be used to predict the probability of failure within a set cycle.
* A Regression model can also be used to predict RUL.

The scatter plots of Sensor 14 in Engine 1 for the train set in shown in Figure 3. The plots show that an RUL value of 30 can be used as a cut-off to generate the label for a classification model because when RUL is under 20 the sensor readings fall outside their normal operating range.
| Train set | Train set |
|:----: |:------:|
| <img src="https://github.com/kuga01/kcu_project_files/blob/main/Business/plot/sensor14_engine1_train.png" width = "450" height = "300">   | <img src="https://github.com/kuga01/kcu_project_files/blob/main/Business/plot/sensor14_engine1_test_tableau.png" width = "450" height = "300">    |
Figure 3, Scatter plot of Sensor 14, Engine 1

#### Tools
* Google Sheets was used for data cleaning and exploratory data analysis.
* Tableau was used to create an interactive dashboard for data visualization.

#### Communication
The findings from the exploratory data analysis of the train set are communicated through an interactive dashboard on tableau. On the dashboard, we can select single or multiple engines and view a horizontal bar plot of maximum RUL for the selected engine(s). The dashboard shows a plot of RUL until engine failure and a normal distribution of Sensor 2 readings. Finally, a scatter plot of sensor 2 and RUL with a linear regression model is displayed at the base of the dashboard. Figure 4 shows a screenshot of the dashboard.

<img src="https://github.com/kuga01/kcu_project_files/blob/main/Business/plot/tableau.png" width = "650" height = "675" class ="center">
Figure 4, Screenshot of tableau interactive dashboard.

