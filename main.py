from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np
app = Flask(__name__)

data= pd.read_csv('cleaned_data.csv')
pipe = pickle.load(open("RidgeModel.pkl",'rb'))
@app.route('/')
def index():
    #locatoin is datas locatoin we are sorting it in order 
    locations = sorted(data['location'].unique());
    return render_template('index.html', locations=locations)
    
#predict funtion that was too be called
@app.route('/predict', methods=['POST'])
def predict():

     location = request.form.get('location')
     bhk = request.form.get('bhk')
     bath = request.form.get('bath')
     sqft = request.form.get('total_sqft')

     print(location, bhk, bath, sqft)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
