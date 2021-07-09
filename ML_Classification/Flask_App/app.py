from flask import Flask, request, render_template
import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chart1')
def chart1():
    df = pd.DataFrame({
        "Target": ["worn", "unworn"],
        "Percent": [0.539442, 0.460558]
    })

    fig = px.bar(df, x="Target", y="Percent", barmode="group")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Class Distribution"
    description = """
    The distribution of classes in the dataset shows that the classes are within 10% 
    of the expected mean of the total classes. Thus, we can say that the dataset is fairly balanced    
    """
    return render_template('notdash.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/chart2')
def chart2():
    df = pd.DataFrame({
        "Model": ['XGBOOST','Random Forest','KNN','SVM', 'Logistic Regression','Stoch Gradient'],
        "AUC": [0.9940, 0.9899, 0.6621, 0.5740, 0.5732, 0.5530]
    })

    fig = px.bar(df, x="Model", y="AUC", barmode="stack")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="AUC comparison"
    description = """
    AUC gives the probability that the random actual positive is ranked higher than random actual negative.
    This is the probability that the classifier assigns high score to the worn class.
    """
    return render_template('notdash2.html', graphJSON=graphJSON, header=header,description=description)
