## Message Classification for Disaster Response

Kalu Chibueze Uga

#### Abstract
Social media has become an essential part of our daily lives. Many people communicate with their family members, friends, and associates via Social Media platforms like Twitter and Facebook. Users of these platforms also express their opinions about different subject matters in their posts. Thus, In the event of a disaster like hurricane, flood, earthquake, or war, it is imperative to monitor messages on the major social media platforms because majority of the victims will turn to social media to seek help and give insight on the severity of the disaster. The desired help could be for water, food, clothing, or first aid. Designing a system that effectively categorizes a message so that an Emergency Response Team (ERT) on ground can send the right help will greatly improve the impact of the ERT. The goal of this project is to build a model to understand natural language disaster messages and appropriately categorize the message based on the inferred topic.

#### Design
* Clean the data and remove duplicates
* Store data in SQLite database
* Perform document preprocessing using spaCy - Remove punctuations, extra space, and make all characters lowercase. Remove words that appear in less than 10 documents and in more than 50% of the corpus.
* Build model using Scikit Learn library - Categorize the corpus into ten groups and use the top fifteen words in each group to deduce the underlying topic.
* Pickle relevant files and use FLASK app for interactive prediction.

#### Data 
The data will comprise of labelled messages related to disaster response in multiple languages (https://www.kaggle.com/landlord/multilingual-disaster-response-messages). The dataset contains 30,000 messages that were collected from news articles and different disasters including super-storm Sandy in the United States in 2012, earthquake in Haiti in 2010, earthquake in Pakistan in 2010, and an earthquake in Chile in 2010.

#### Algorithm
Modeling was performed using six combinations of CountVectorizer and Term Frequency - Inverse Document Frequency (Tfidf) with (Latent Dirichlet Allocation, Latent Semantic Allocation, and Non-Negative Matrix Factorization). Tfidf and Latent Dirichlet Allocation was the best combination because the topics were more interpretable based on the top ten messages in the topic. Also, this combination identified a topic on "Donations" which other combinations could not identify. Figure 1 shows a plot of topics and the count of documents in the topics.

<img src="https://github.com/kuga01/kcu_project_files/blob/main/NLP_Unsupervised_Learning/plots/topic_doc_count.png" width = "750" height = "450">
Figure 1, Plot of count of documents in topic.


The ten inferred topics and cluster of topics 4 and 7 are shown in figure 2.

| 2a, Inferred topics | 2b, Cluster of topics 4 and 7 |
|:----: |:------:|
| <img src="https://github.com/kuga01/kcu_project_files/blob/main/NLP_Unsupervised_Learning/plots/top_10_topics.png" width = "450" height = "350">   | <img src="https://github.com/kuga01/kcu_project_files/blob/main/NLP_Unsupervised_Learning/plots/topic4_topic7_clusters.png" width = "450" height = "350">    |
Figure 2, Top 10 topics and cluster of topics 4 and 7

*Prediction and similar document*

Finally, the. model was tested on the unseen message below; 

        Sample Message = ["We need food and medical supplies. The kids
                          also need blankets and clothing"]


        Topic Category is "AID_RELATED - FOOD,WATER,SHELTER,MEDICINE"


Using cosine similarity, the most similar message in our corpus to the Sample message is:

        we have clothes for all ages and brand new shoes and boots we 
        have baby items like diapers car seats high chair ect we also 
        have hygine products like wipes toothbrushes toothpaste ect we 
        also have some kids toys and stuffed animals even a bike and we 
        also have some non perishable foods and blankets

#### Tools
1. Pandas for data cleaning.
2. SQLite database for data storage.
3. spaCy for corpus preprocessing.
4. Scikit Learn and Numpy for data manipulation
5. Matplotlib and seaborn for data visualization
6. FLASK app for interactive prediction.

#### Communication
After building a model to categorize disaster messages, the prediction has been made user friendly through FLASK application. Required information like "best_lda_model", "nlp object", "vectorizer object", and "topic_keywords data frame" were saved and loaded in the FLASK app script. Figure 3 shows the predicted group for the input message below;

        ["We need food and medical suppies. The kids also need blankets 
        and clothing"] 

| 3a, Flask App Home | 3b, Result |
|:----: |:------:|
| <img src="https://github.com/kuga01/kcu_project_files/blob/main/NLP_Unsupervised_Learning/plots/nlp_app1.png" width = "450" height = "250">   | <img src="https://github.com/kuga01/kcu_project_files/blob/main/NLP_Unsupervised_Learning/plots/nlp_app2.png" width = "450" height = "250">    |
Figure 3, Topic Modeling Prediction using Flask App.

