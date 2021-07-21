# -*- coding: utf-8 -*-
"""
Created on Wed July 21 13:57:01 2021

@author: utsav gada
"""

import pickle
import numpy as np
import pandas as pd
import streamlit as st

pickle_in = open('bostonhouseprice.pkl', 'rb')
regressor=pickle.load(pickle_in)

def Home():
    return "Welcome"


def predict(crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,b,lstat):
    
    prediction = regressor.predict([[crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,b,lstat]])
    print(prediction)
    return prediction
    
def main():
    st.title("Boston House Price Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Boston House Price Prediction </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    crim = st.text_input("Per capita crime rate by town","Eg. 0.00632")
    zn = st.text_input("Proportion of residential land zoned for lots over 25,000 sq.ft.","Eg. 18.0")
    indus = st.text_input("Proportion of non-retail business acres per town","Eg. 2.31")
    chas = st.text_input("Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)","Eg. 0.0 or 1.0")
    nox = st.text_input("Nitric oxides concentration","Eg. 0.538")
    rm = st.text_input("Average number of rooms per dwelling","Eg. 6.575")
    age = st.text_input("Proportion of owner-occupied units built prior to 1940","Eg. 65.2")
    dis = st.text_input("Weighted distances to five Boston employment centres","Eg. 4.0900")
    rad = st.text_input("Index of accessibility to radial highways","Eg. 1.0")
    tax = st.text_input("Full-value property-tax rate per 10,000 usd","Eg. 296.0")
    ptratio = st.text_input("pupil-teacher ratio by town","Eg. 15.3")
    b = st.text_input("B 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town","Eg. 396.90")
    lstat = st.text_input("% Lower status of the population","Eg. 4.98")
    
    result=""
    if st.button("Predict"):
        result=predict(crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,b,lstat)
    st.success('The output is {}'.format(result))
    
    
    
if __name__=="__main__":
    main()