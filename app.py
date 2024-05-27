from flask import Flask, url_for, redirect, request, render_template

import pickle
import numpy as np
from xgboost import XGBClassifier

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/input', methods = ['POST'])
def input():
    url = request.form['url-input']

    #change to list (temporary)
    string_list = url.split(",")
    integer_list = [int(item) for item in string_list]
    
    with open('XGBoostClassifier.pickle.dat', 'rb') as file:
        loaded_model = pickle.load(file)

    features = integer_list

    # Make predictions
    new_data = np.array([features],dtype=object)
    prediction = loaded_model.predict(new_data)

    if prediction == 0 :
        res = 'Safe'
    elif prediction == 1 :
        res = 'Phishing'
    else :
        res = "Error"

    return render_template('result.html', result = res)

@app.route('/results', methods = ['GET'])
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run()