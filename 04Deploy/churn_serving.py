import pickle
from flask import Flask, request, jsonify
import requests
import numpy as np
import os

# request: To get the content of a POST request
# jsonsify: To respond with JSON

def predict_single(customer, dv, model):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]


filepath = 'churn_model.bin'
if os.path.exists(filepath):
    file = open(filepath, 'rb')
    dv, model = pickle.load(file)
    file.close()
else:
    print("File not present at desired location")

app = Flask('churn')
@app.route('/predict', methods=['POST'])
def predict():
    customer =  request.get_json()
    prediction = predict_single(customer, dv, model)
    churn = prediction >= 0.5

    # Prepare response
    result = {
        'churn_probability': float(prediction),
        'churn': bool(churn),
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)