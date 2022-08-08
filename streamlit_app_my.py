import pickle

import streamlit as st
import pandas as pd
import preprocess_data


model_file = 'models/best_rf_model.b'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)


def predict(features: dict):
    df = pd.DataFrame.from_dict([features], orient='columns')
    df = preprocess_data.preprocess(df.copy())

    preds = model.predict(df)

    return float(preds[0])

st.markdown("<h1 style='text-align: center; color: black;'>Health Insurance Price Forecast</h1>", unsafe_allow_html = True)


features = {}

expander = st.expander("Personal Information")

with expander:
    features['age'] = st.slider('What is your age?', help = 'The slider can be moved using the arrow keys.', min_value = 0, max_value = 100, step = 1)

    features['sex'] = 1 if st.selectbox('What is your gender?', ['Female', 'Male']) == 'Yes' else 0

    features['bmi'] = st.slider('What is your BMI (Body Mass Index)?', help = 'The slider can be moved using the arrow keys.', min_value = 0.0, max_value = 100.0, step = 0.1)

    features['children'] = st.slider('How many children do you have?', help = 'The slider can be moved using the arrow keys.', min_value = 0, max_value = 10, step = 1)

    features['smoker'] = 1 if st.selectbox('Do you smoke?', ['Yes', 'No']) == 'Yes' else 0

    features['region'] = st.selectbox('In what US region do you live?', ['Southwest', 'Southeast', 'Northwest', 'Northeast'])

if st.button('Predict Cost'):
    value = predict(features)
    st.write(f'Your insurance would cost {round(value, 2)} USD.')