from flask import Flask
from flask import request
from flask import jsonify

import pandas as pd

import preprocess_data
from train import load_pickle

MODEL_NAME = 'models/best_rf_model.b'

app = Flask('insurance-prediction')

def predict(features: dict):
    df = pd.DataFrame.from_dict([features], orient='columns')
    df = preprocess_data.preprocess(df.copy())

    preds = model.predict(df)

    return float(preds[0])


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    data = request.get_json()
    pred = predict(data)

    result = {
        "charges": pred
    }
    return jsonify(result)


if __name__ == "__main__":
    model = load_pickle(MODEL_NAME)
    app.run(debug=True, host='0.0.0.0', port=9696)
