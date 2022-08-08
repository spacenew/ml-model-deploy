from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd
import pickle
import preprocess_data

model_file = 'models/best_rf_model.b'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

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
    app.run(debug=True, host='0.0.0.0', port=9696)
