# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 11:45:03 2021

@author: noopa
"""


import numpy as np
import pickle
import pandas as pd
from flask import Flask, request
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)
pickle_in = open(r"\Users\Clifo\OneDrive\Documents\project\classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = classifier.predict(final_features)
    species = {0: 'Bream', 1: 'Parkki',2: 'Perch', 3: 'Pike', 4: 'Roach', 5: 'Smelt', 6: 'Whitefish'}
    
    return render_template('index.html', prediction_text='The fish belong to species {}'.format(species[prediction[0]]))
    
    


if __name__=='__main__':
    app.run()