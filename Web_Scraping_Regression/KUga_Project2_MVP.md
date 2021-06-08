## Predicting Final Points in European Soccer Leagues by Linear Regression 

---
Kalu Chibueze Uga


#### Goal
---

The goal of this project is to predict the total points a team can achieve based on the primary features that contribute to the success of a soccer club. These features include goal difference, total value of a squad, and many more.

A plot of goal difference againt total points in the figure below  shows a strong linear relationship. Also, the error shows a random distribution, and the probability plot shows that residuals are normally distributed. Given the observations, we can use a linear regression model on the data set.
<img src="https://github.com/kuga01/kcu_project_files/blob/main/Web_Scraping_Regression/plots/gd_var_plot.png" width = "850" height = "325">

After analysing all the features that were scrapped from transfermarkt.com and whoscored.com, I have decided to work with fifteen features that show a decent correlation with total points. 

While performing baseline regression analysis, I started with an initial model with no transformations, R-squared was 0.9191974396753099 and my constants were;

```
GD : 0.54
GF : 0.17
SHOTS_OT_PG : -2.63
POSSESSION_PERCENT : 0.13
SHOTS_PG : 0.41
TOTAL_MARKET_VALUE (m€) : 0.01
PASS_PERCENT : 0.04
DRIBBLES_PG : -0.27
OFFSIDES_PG : -0.45
YC : 0.01
FOULED_PG : -0.12
TACKLES_PG : 0.05
INTERCEPTIONS_PG : 0.20
RC : 0.19
AERIALS_WON : 0.06
```
Polynomial transformation (order 2) was applied to PASS_PERCENT because the relationship with POINTS looked parabolic. However, this addition did not improve my validation R-squared (0.9191491834221109) so this added feature was dropped. I added a logarithmic function on "TOTAL_MARKET_VALUE" and noticed a minor increase in validation R-squared (0.9193859286401059).
Finally, I added a division interaction and noticed an increase in validation R-squared to 0.9213417669277634.
The figure below shows how the test prediction got better with the added features.

| Initial Model | Final Model with Feature Engineering |
|:----: |:------:|
| <img src="/Users/amyphillip/Desktop/Metis/project_2_webscrap_linreg/Web_Scraping_Regression/plots/initial_model.png" width = "450" height = "300">   | <img src="/Users/amyphillip/Desktop/Metis/project_2_webscrap_linreg/Web_Scraping_Regression/plots/fe_model.png" width = "450" height = "300">    |

The normal distribution of residuals on the test dataset is shown on the histogram and probability plots below.

<img src="/Users/amyphillip/Desktop/Metis/project_2_webscrap_linreg/Web_Scraping_Regression/plots/hist_prob.png" width = "850" height = "325">

#### Error Analysis
---

The error values from the current analysis shows that;

Root Mean Square (RMSE) (train/val): 4.761
Root Mean Square (RMSE) test         : 4.639

Mean Absolute Error (MAE) (train/val): 3.735
Mean Absolute Error (MAE) test         : 3.693

So far the model prediction is within +/- 5 points of the actual points. The constants from the model are shown below.

```
GD : 0.54
GF : -0.39
SHOTS_OT_PG : -2.44
POSSESSION_PERCENT : 0.12
SHOTS_PG : 2.66
TOTAL_MARKET_VALUE (m€) : 0.01
PASS_PERCENT : 0.01
DRIBBLES_PG : -0.22
OFFSIDES_PG : -0.41
YC : 0.01
FOULED_PG : -0.15
TACKLES_PG : 0.02
INTERCEPTIONS_PG : 0.20
RC : 0.22
AERIALS_WON : 0.05
TOTAL_MARKET_VALUE (m€)_LOG : -0.91
GF_/SHOTS_PG : 7.35
```

#### Further Analysis
---
I have applied ridge regression with alpha = 1 and noticed that second order polynomial did not improve the mode. 

Linear Regression train/val R^2: 0.915
Linear Regression test R^2: 0.915

Also, feature engineering did better than the ridge regresion model with alpha = 1.0

The next steps are:
* Add Ridge/Lasso analysis to find optimum lambda and to eliminate features of less importance.
* Implement time series approach to find a model that will predict total points in the English Premier League
