
import pandas as pd
import streamlit as st 
from xgboost.sklearn import XGBRegressor
from pickle import load

st.title('Power Plant Energy Prediction')

st.sidebar.header('Input Parameters')

def user_input_features():
    temp = st.sidebar.number_input('Temperature, in degrees Celsius')
    exh = st.sidebar.number_input('Exhaust Vacuum, in cm Hg')
    amp = st.sidebar.number_input('Ambient Pressure, in millibar')
    hum = st.sidebar.number_input("Relative Humidity, in percentage")
    data = {'Temperature':temp,
            'Exhaust Vacuum':exh,
            'Ambient Pressure':amp,
            'Relative Humidity':hum}
    features = pd.DataFrame(data,index = [0])
    return features 
    
input_df = user_input_features()
st.subheader('User Input parameters')
st.write(input_df)


# load the model from disk
model = load(open('C:/Users/Rahul/Desktop/DS Projects/xgboost_model.pkl', 'rb'))

prediction = ""
if st.button('Check for Result'):
    prediction = model.predict(input_df)

st.subheader('Predicted Result, in MW')
st.write(prediction)



