import pandas as pd
import numpy as np
import pickle
#import xgboost
#import flasgger
#from flasgger import Swagger
from flask import Flask, request, render_template
#from pandas.io.json import json_normalize
import json


# with open('G:\iNeuron\Dota\heroes.json') as f:
#     d = json.load(f) 
# data3 = json_normalize(d['heroes']) 


app= Flask(__name__)

app.jinja_env.filters['zip'] = zip
#Swagger(app)

pickle_in= open('rnd_clf.pkl', 'rb')
#pickle_home= open('rnd_clf_house.pkl', 'rb')
#dota_rnd= open('dota_rnd.pkl', 'rb')
classifier= pickle.load(pickle_in)
# house_rent= pickle.load(pickle_home)
# dote= pickle.load(dota_rnd)

columns_house= [
 'sqfeet',
 'beds',
 'baths',
 
 'lat',
 'long', 'state']


col_name= ['name', 'age', 'height(cm)', 'weight', 'systolic(B.P.-Upper)', 'diastolic(B.P.-Lower)']
all_col= ['name', 'age', 'height', 'weight', 'ap_hi', 'ap_lo', 'smoke', 'alco', 'active','cholesterol', 'gluc']

#drop_down= ['gender', 'smoke', 'alco','active', 'cholesterol', 'gluc']

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/fill_form')
def fill_form():
    return render_template('form.html', columns= col_name)

@app.route('/predict')
def predict_route_authentication():
    
    name= request.args.get('name')
    age= request.args.get('age')
    gender= request.args.get('gender')
    height= request.args.get('height')
    weight= request.args.get('weight')
    ap_hi= request.args.get('ap_hi')
    ap_lo= request.args.get('ap_lo')
    smoke= request.args.get('smoke')
    alco= request.args.get('alco')
    active= request.args.get('active')
    cholesterol_2= request.args.get('cholesterol_2')
    cholesterol_3= request.args.get('cholesterol_3')
    gluc_2= request.args.get('gluc_2')
    gluc_3= request.args.get('gluc_3')

    prediction= classifier.predict([[age, gender, height, weight, ap_hi, ap_lo, smoke, alco, active, cholesterol_2, cholesterol_3, gluc_2, gluc_3]])
    #pred_proba= classifier.predict_proba([[age, gender, height, weight, ap_hi, ap_lo, smoke, alco, active, cholesterol_2, cholesterol_3, gluc_2, gluc_3]])



    return 'The prediction value is '+str(prediction)




@app.route('/products')
def fill_form_home():
    print('hello')
    return render_template('products.html')

def mapping(val, col_1, col2):
    if val=='Low':
        col_1= 0
        col_2= 0
    elif val== 'Medium':
        col_1= 1
        col_2= 0
    else:
        col_1= 0
        col_2= 1
    return col_1, col2

def one_map(val):
    if val==0:
        val= 'No'
    else:
        val= 'Yes'
    return val


@app.route('/result', methods= ['GET', 'POST'])
def result():
    if request.method=='POST':
        name= request.form.get('name')
        age= request.form.get('age')
        gender= request.form.get('gender')
        height= request.form.get('height(cm)')
        weight= request.form.get('weight')
        ap_hi= request.form.get('systolic(B.P.-Upper)')
        ap_lo= request.form.get('diastolic(B.P.-Lower)')
        smoke= request.form.get('smoke')
        alco= request.form.get('alco')
        active= request.form.get('active')
        cholesterol= request.form.get('cholesterol')
        #cholesterol_3= request.form.get('cholesterol_3')
        gluc= request.form.get('gluc')
        #gluc_3= request.form.get('gluc_3')

        #posts=[40, 60]
        #res= 55
        cholesterol_2= 0
        cholesterol_3= 0
        gluc_2= 0
        gluc_3= 0

        cholesterol_2, cholesterol_3= mapping(cholesterol, cholesterol_2, cholesterol_3)
        gluc_2, gluc_3= mapping(gluc, gluc_2, gluc_3)

        smoke_= one_map(smoke)
        alco_= one_map(alco)
        active_= one_map(active)
        gender_= one_map(gender)

        

        print('------------- GENDER IS--------', gender, cholesterol, gluc, name)
        values= [age, gender, height, weight, ap_hi, ap_lo, smoke, alco, active,cholesterol_2, cholesterol_3, gluc_2, gluc_3]
        res_val= [age, gender, height, weight, ap_hi, ap_lo, smoke_, alco_, active_, cholesterol, gluc]
        all_col_= ['age', 'gender', 'height', 'weight', 'systolic(B.P.-Upper)', 'diastolic(B.P.-Lower)', 'smoke', 'alco', 'active','cholesterol', 'gluc']
        prediction= classifier.predict([values])
        pred_proba= classifier.predict_proba([values])
        print('prediction =', prediction, 'probability =', pred_proba)
        return render_template('result.html', columns= all_col_, values= res_val, pred= prediction, prob= pred_proba[0][0], name= name)
    else:
        #message= 'First Fill the form'
        return render_template('form.html', columns= col_name)




# @app.route('/result_home', methods= ['POST'])
# def result_home():
#     pass

# @app.route('/dota_form')
# def dota_form():

#     names= pd.DataFrame(columns= ['id', 'name'])
#     #names.head()

#     for i in range(data3.shape[0]):
#         names = names.append({'id': data.columns[i+5], 'name': data3['localized_name'][i]}, ignore_index= True)
    
#     print(names.head())
#     return render_template('dota_form.html', dota_id=names['id'], dota_names= names['name'])

# @app.route('/predict_file', methods= ['POST'])
# def predict_file():
#     file_= request.files.get('file')
#     df_test= pd.read_csv(file_)
#     print(df_test.head())
#     #request.files.g
#     prediction= classifier.predict(df_test)
#     return 'Predicted values of the CSV are '+ str(list(prediction))




if __name__=='__main__':
    app.run(debug= True)