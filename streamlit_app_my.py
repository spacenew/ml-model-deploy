import streamlit as st
import pandas as pd

import pickle


model_file = 'model_rf.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)


def predict(answers):
    df = pd.DataFrame(answers.items()).T
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    df.reset_index(drop = True)
    df['region'] = df['region'].map({'Southwest': 0, 'Southeast': 1, 'Northwest': 2, 'Northeast': 3})

    prediction = model.predict(df)
    
    return float(prediction)

st.markdown("<h1 style='text-align: center; color: black;'>Health Insurance Price Forecast</h1>", unsafe_allow_html = True)


answers = {}

expander = st.expander("Personal Information")

with expander:
    answers['age'] = st.slider('What is your age?', help = 'The slider can be moved using the arrow keys.', min_value = 0, max_value = 100, step = 1)

    answers['sex'] = 1 if st.selectbox('What is your gender?', ['Female', 'Male']) == 'Yes' else 0

    answers['bmi'] = st.slider('What is your BMI (Body Mass Index)?', help = 'The slider can be moved using the arrow keys.', min_value = 0.0, max_value = 100.0, step = 0.1)

    answers['children'] = st.slider('How many children do you have?', help = 'The slider can be moved using the arrow keys.', min_value = 0, max_value = 10, step = 1)

    answers['smoker'] = 1 if st.selectbox('Do you smoke?', ['Yes', 'No']) == 'Yes' else 0

    answers['region'] = st.selectbox('In what US region do you live?', ['Southwest', 'Southeast', 'Northwest', 'Northeast'])

if st.button('Predict Cost'):
    value = predict(answers)
    st.write(f'Your insurance would cost {round(value, 2)} USD.')