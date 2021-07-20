## Message Classification for Disaster Response

Kalu Chibueze Uga

#### Abstract
Social media has become an essential part of our daily lives. Many people communicate with their family members, friends, and associates via Social Media platforms like Twitter and Facebook. Users of these platforms also express their opinions about different subject matters in their posts. Thus, In the event of a disaster like hurricane, flood, earthquake, or war, it is imperative to monitor messages on the major social media platforms because majority of the victims will turn to social media to seek help and give insight on the severity of the disaster. The desired help could be for water, food, clothing, or first aid. Designing a system that effectively categorizes a message so that an Emergency Response Team (ERT) on ground can send the right help will greatly improve the impact of the ERT. The goal of this project is to build a model to understand natural language disaster messages and deduce the help that is needed.

#### Data 
The data will comprise of labelled messages related to disaster response in multiple languages (https://www.kaggle.com/landlord/multilingual-disaster-response-messages). The dataset contains messages that were collected from news articles and different disasters including super-storm Sandy in the United States in 2012, and an earthquake in Chile in 2010.

#### Analysis
For a base analysis, I have use spaCy for preprocessing, CountVectorizer for my document-word matrix, and Latent Dirichlet Allocation (LDA) for topic modeling. I used GridSearch to find best number of components and learning rate for LDA are 10 and 0.9 respectively. After reviewing the top ten documents in the top ten topics (using the top fifteen words in each topic), I came up with the following interpretations for each topic:

Topic 0 = AID/INFORMATION RELATED 
Topic 1 = NEWS UPDATE
Topic 2 = AID_RELATED - FOOD,WATER,SHELTER,MEDICINE
Topic 3 = INFRASTRUCTURE_RELATED / JOB_REQUEST
Topic 4 = SEVERE WEATHER UPDATE
Topic 5 = OPINION/OTHER_REQUESTS
Topic 6 = EARTHQUAKE UPDATE
Topic 7 = CLOTHING/MEDICAL_PRODUCTS
Topic 8 = TRANSPORT/TRAVEL INFORMATION
Topic 9 = SECURITY/HEALTH/ENVIRONMENT CONCERNS

I have used TruncatedSVD and KMEANS cluster to plot the cluster of points by topic as shown in figure 1. 

<img src="/Users/amyphillip/Desktop/Metis/Project_5_NLP/NLP_Unsupervised_Learning/plots/cluster_of_points.png" width = "450" height = "450"> 
Figure 1, Cluster of 10 topics

Finally, I have used a distance matrix to find the most similar document in a topic for a given message data. For instance, given the sample message below,

Sample_Message = ["We need food and medical supplies. The kids also need blankets and clothing"]

Topic Category is "AID_RELATED - FOOD,WATER,SHELTER,MEDICINE"

The most similar document in the topic group is:

"we live in la pleine since tuesday we ve been sleeping on the street hunger is killing us"