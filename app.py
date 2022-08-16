import pandas as pd
import streamlit as sl

from packages.train import load_pickle

MODEL_NAME = 'models/best_rf_model.b'


def prepare_features(features: dict):
    df = pd.DataFrame.from_dict([features], orient='columns')

    df['region'] = df['region'].map(
        {'Southwest': 0,
         'Southeast': 1,
         'Northwest': 2,
         'Northeast': 3})

    prediction = model.predict(df)

    return float(prediction)


def run_forecast():
    sl.markdown(
        "<h1 style='text-align: center; color: Green;'"
        ">Forecast Health Insurance Price</h1>",
        unsafe_allow_html=True)
    expander = sl.expander("Personal Information")

    input_answers = dict()

    with expander:
        input_answers['age'] = sl.slider('What is your age?',
                                         min_value=0,
                                         max_value=100,
                                         step=1)
        input_answers['sex'] = True if sl.selectbox('What is your gender?',
                                                 ['Female',
                                                  'Male']) == 'Yes' else False
        input_answers['bmi'] = sl.slider('What is your Body Mass Index?',
                                         min_value=0.0,
                                         max_value=100.0,
                                         step=0.1)
        input_answers['children'] = sl.slider('How many children do you have?',
                                              min_value=0,
                                              max_value=10,
                                              step=1)
        input_answers['smoker'] = True if \
            sl.selectbox('Do you smoke?', ['Yes', 'No']) == 'Yes' else False

        input_answers['region'] = sl.selectbox(
            'what US region do you live?',
            ['Southwest', 'Southeast', 'Northwest', 'Northeast'])

    if sl.button('Predict Cost'):
        charges = prepare_features(input_answers)
        sl.write(f'Your insurance would cost {round(charges, 0)} USD.')


if __name__ == "__main__":
    model = load_pickle(MODEL_NAME)
    run_forecast()
