# Predicting Final Points in European Soccer Leagues by Linear Regression 
Kalu Chibueze Uga

## Abstract
European soccer has set the standard accross the world in viewership, transfer fees, revenue, and fantasy sports. The goal of this project is to predict the total points a team can achieve based on the primary features that contribute to the success of a soccer club. These features include goals scored, total value of a squad, and many more. Clubs have been spending  lots of money every year to acquire players that will boost the teams chance of securing more points over the course of a soccer season.

## Design
A plot of goals scored againt total points in Figure 1 shows a decent linear relationship. Also, the error shows a random distribution, and the probability plot shows that residuals are normally distributed. Given these observations, we can use a linear regression model on the dataset.

<img src="https://github.com/kuga01/kcu_project_files/blob/main/Web_Scraping_Regression/plots/why_regression_diagnostics.png" width = "850" height = "325" class ="center"> Figure 1

Current trend from the data set shows that teams with a high value squad stand a better chance of achieving more points in a season because the overall quality of the players are better. The teams passing accuracy, chance creation, and goal convertion rate is higher.

## Data
Data for twelve seasons (2009 to 2020) and the top five European leagues were collected from [transfermarkt](http://transfermarkt.com/) and [whoscored](http://whoscored.com/).
* Total market value of all the teams was gathered from [transfermarkt](http://transfermarkt.com/).
* Team statistics (offensive and defensive) were gathered from [whoscored](http://whoscored.com/).
* The total data consists of 1176 rows and 31 columns.

## Algorithm
*Data acquisition with Selenium*

1. Collect season data from two tables on transfermarkt,com. 
2. Merge the tables so that teams are ordered based on position on the league table
3. Collect data from four tables on whoscored.com. 
4. Merge tables so that teams are ordered by position on the league table.
5. Perform a LEFT JOIN at the end of every "season loop" to merge data from the two sources and save the resulting dataframe in the correct league dictionary.

*Data cleansing*

1. Ensured that there were no null values. 
2. Edit the Total Market Value column so that the unit is in million Euros. 
3. Changed column names to look pythonic.
4. Updated the data types of all the columns.
5. Visualized some features to find trends.

## Tools
- Selenium was used to scrap the source websites dynamically.
- Numpy and Pandas were used for data manipulation.
- Matplotlib and seaborn were used for visualization

## Communication
Backward elimination method was used to eliminate features that would not improve the model more than it would by chance. Starting with a combination of ten features, this method trimed it down to six primary features. Feature engineering was performed to add three more features that improved the R-squared of the validation dataset. The coefficients are shown in Figure 2.

<img src="/Users/amyphillip/Desktop/Metis/project_2_webscrap_linreg/Web_Scraping_Regression/plots/coefficients.png" width = "650" height = "225" class ="center"> 
Figure 2


Furthermore, error analysis from validation and regularization of the primary model and the feature engineering (FE) model showed that the feature engineering model with k-fold cross validation had the lowest mean absolute error (MAE) as shown in Figure 3 below. Thus, the FE model is the model of choice.

| Backward Elimination | MAE Comparison |
|:----: |:------:|
| <img src="/Users/amyphillip/Desktop/Metis/project_2_webscrap_linreg/Web_Scraping_Regression/plots/backward_elimination.png" width = "450" height = "300">   | <img src="/Users/amyphillip/Desktop/Metis/project_2_webscrap_linreg/Web_Scraping_Regression/plots/mae_plot.png" width = "450" height = "300">    |
Figure 3

The close distribution of points around the model line and the distribution of residuals around the horizontal line in figure 4 shows that the model can predict about 70 percent of points. The model can be further improved by more feature engineering and collecting the average of the coefficients from k-fold cross validation.

<img src="/Users/amyphillip/Desktop/Metis/project_2_webscrap_linreg/Web_Scraping_Regression/plots/cv_fe1.png" width = "750" height = "225" class ="center"> 
Figure 4

Finally, the error distribution in Figure 5 satisfies the assumption that linear regression residuals should be normally distributed.  Points on the probabiity plot are close to the normality line.

<img src="/Users/amyphillip/Desktop/Metis/project_2_webscrap_linreg/Web_Scraping_Regression/plots/cv_fe2.png" width = "650" height = "225" class ="center">
Figure 5
