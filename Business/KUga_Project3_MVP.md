## Predictive Maintenance of Simulated Aircraft Gas Turbine Engines

Kalu Chibueze Uga

#### Abstract
Mechanical failure is expected of all mechanical equipment and it could have severe consequences like termination of contract due to downtime accrued. The ability to correctly predict equipment failure will help companies improve utilization of equipment parts and avoid unnecessary downtime. Predictive maintenance via machine learning is designed to help predict the probability of failure so that maintenance can be scheduled in advance and carried out only when needed. The goal of this project is to show that using historic dataset, we can find failure patterns that could be used to predict failure in the future. 

#### Data 
The dataset will be NASA TurboFan Engine data provided by NASA. The data consists of sensor readings of the operating conditions of one hundred simulated aircraft gas turbine engines. Three files were provided; a train set, a test set, and the Remaining Useful Life (RUL) of the test set. The engines in the train set were operating until they failed, whereas, the engines in the test set have not failed. The rows in the dataset represent data collected every cycle for every engine.The train and test sets consist of Engine ID, Cycle, three operation settings, and twenty three sensor readings as features. 

#### Exploratory Data Analysis
The test data showed that some sensor readings and operation mode were constant for all the engines. These constant features were droped. The features that showed dependence on settings were retained. Figure 1 shows feature dependence on operation settings.
| Constant feature | Varying feature |
|:----: |:------:|
| <img src="https://github.com/kuga01/kcu_project_files/blob/main/Business/plot/mode3_sensor2.png" width = "450" height = "300">   | <img src="https://github.com/kuga01/kcu_project_files/blob/main/Business/plot/mode1_sensor2.png" width = "450" height = "300">    |
Figure 1, Feature dependence on operation settings.

A plot of the distribution of SENSOR 9 shows a normal distribution as seen in Figure 2a. Figure 2b shows the current cycle and RUL of the first 10 engines.
| 2a, Distribution of SENSOR 9 | 2b, Cycle and RUL of first 10 engines |
|:----: |:------:|
| <img src="https://github.com/kuga01/kcu_project_files/blob/main/Business/plot/dist_s9.png" width = "450" height = "300">   | <img src="https://github.com/kuga01/kcu_project_files/blob/main/Business/plot/cycle_rul.png" width = "450" height = "300">    |
Figure 2, Distribution and cycle plots.

#### Model
* Use a classification model to predict the probability of failure within a given cycle.
* Use a regression model to predict remaining useful life.

Correctly predicting over 70 percent of failures using the proposed models will help us keep our current contract and boost our ability to secure future contracts with our clients because it will show transparency through communication. Clients are generally pleased to know that an equipment maintenance is scheduled before an expected failure rather than a reactive approach to repair a failed equipment.

