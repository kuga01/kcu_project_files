## Message Classification for Disaster Response

Kalu Chibueze Uga

#### Abstract
Social media has become an essential part of our daily lives. Many people communicate with their family members, friends, and associates via Social Media platforms like Twitter and Facebook. Users of these platforms also express their opinions about different subject matters in their posts. Thus, In the event of a disaster like hurricane, flood, earthquake, or war, it is imperative to monitor messages on the major social media platforms because majority of the victims will turn to social media to seek help and give insight on the severity of the disaster. The desired help could be for water, food, clothing, or first aid. Designing a system that effectively categorizes a message so that an Emergency Response Team (ERT) on ground can send the right help will greatly improve the impact of the ERT. The goal of this project is to build a model to understand natural language disaster messages and deduce the help that is needed.

#### Design
* Apply several Natural Language Processing classification algorithms like naive Bayes and Support Vector Machines.
* Pick the best algorithm and test performance on unseen data.

#### Data 
The data will comprise of labelled messages related to disaster response in multiple languages (https://www.kaggle.com/landlord/multilingual-disaster-response-messages). The dataset contains messages that were collected from news articles and different disasters including super-storm Sandy in the United States in 2012, and an earthquake in Chile in 2010.

#### Tools
* Pandas will be used for data cleaning and manipulation.
* Matplotlib and seaborn for data visualization.
* Flask will be used to create an interactive dashboard.

#### MVP Goal
Make prediction on the category of a text using two models and compare their performance.