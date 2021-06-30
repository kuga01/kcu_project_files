## Detecting Wear on a Computer Numerically Controlled Mill Tool

Kalu Chibueze Uga

#### Abstract
Advanced manufacturing and large scale production depend highly on Computer Numerically Controlled (CNC) machining. However, many companies are not efficient because they have a poor approach to mill tool failure management. Mill tool wear can lead to end products that will fail final Quality Check, waste of raw material, waste of coolant materials, and can result in unnecessary financial expenses if the mill tool breaks. The goal of this project is to predict wear on a CNC milling tool so that the milling tool can be replaced before products are ruined due to poor cutting structure of the worn mill tool.

#### Design
* The goal is to find the classification model that has the highest probability of predicting wear in mill tools. 
* A measure of success will be to correctly predict over 70 percent of wear in milling tool.
* It is assumed that third party sensors (position, velocity, vibration, current, voltage, etc) are operating as expected and the sensor readings are correct.

#### Data 
The data will be Milling Data Set from NASA Ames Prognostics Data Repository (http://ti.arc.nasa.gov/project/prognostic-data-repository), NASA Ames Research Center, Moffett Field, CA.
The dataset consists of a time series experiment from 18 CNC machines for variations of tool condition, feed rate, and clamp pressure with a sampling rate of 100 ms. The output of each experiment shows tool condition (worn or unworn), finalized machining (yes/no), and visual inspection (yes/no).

#### Tools
* Pandas will be used for data cleaning and manipulation.
* Matplotlib and seaborn for data visualization.
* Tableau will be used to create an interactive dashboard for data visualization.

#### MVP Goal
Predict mill tool wear using at least two classification models and compare their predictions.