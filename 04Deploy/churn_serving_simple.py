# Here contains:
# The function for a single customer prediction
# Pickle package to save/load the model
# dict with costumer features 
# The code for loading the model
# The code for applying the model to a customer


import pickle
import numpy as np
import os


def predict_single(customer, dv, model):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]

#Loading the Model
#with open('churn_model.pkl', 'rb') as f_in:
#    dv, model = pickle.load(f_in)

filepath = 'churn_model.bin'
if os.path.exists(filepath):
    file = open(filepath, 'rb')
    dv, model = pickle.load(file)
    file.close()
else:
    print("File not present at desired location")
    

customer = {
    'customerid': '8879-zkjof',
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'no',
    'dependents': 'no',
    'tenure': 41,
    'phoneservice': 'yes',
    'multiplelines': 'no',
    'internetservice': 'dsl',
    'onlinesecurity': 'yes',
    'onlinebackup': 'no',
    'deviceprotection': 'yes',
    'techsupport': 'yes',
    'streamingtv': 'yes',
    'streamingmovies': 'yes',
    'contract': 'one_year',
    'paperlessbilling': 'yes',
    'paymentmethod': 'bank_transfer_(automatic)',
    'monthlycharges': 79.85,
    'totalcharges': 3320.75
}

prediction = predict_single(customer, dv, model)

print('prediction: %.3f' % prediction)

if prediction >= 0.5:
    print('verdict: Churn')
else:
    print('verdict: Not churn')
