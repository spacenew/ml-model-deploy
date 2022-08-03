# libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import RandomizedSearchCV, KFold

import pickle

# constants
rs = 2022

# functions
def run_model(model, print_values = True, return_predictions = False):
    
    model.fit(X_train, y_train)
    y_predictions = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_predictions)
    rmse = mean_squared_error(y_test, y_predictions, squared=False)
    if print_values:
        print(f"MAE: {round(mae, 3)}")
        print(f"RMSE: {round(rmse, 3)}")
    if return_predictions:
        return y_predictions, mae, rmse
    return mae, rmse


# load data
print('Loading data...\n')
df = pd.read_csv('insurance.csv')

# prepare data
print('Preparing data...\n')

df['sex'] = df['sex'].map({"female": 0, "male": 1})
df['region'] = df['region'].map({'southwest': 0, 'southeast': 1, 'northwest': 2, 'northeast': 3})
df['smoker'] = df['smoker'].map({"yes": 1, "no": 0})

X = df.drop('charges', axis = 1)
y = df['charges']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = rs)

# fit and train the model
print('Fitting and training the RandomForestRegressor...')

rf = RandomForestRegressor(random_state = 2022)

params = {
    'n_estimators': [10, 30, 50, 100],
    'max_features': ['auto', 'sqrt', 'log2'],
    'min_samples_split': [10, 20, 30, 50],
    'bootstrap': [True, False]
}

CV = KFold(n_splits=5, shuffle=True, random_state=2022)

rf_search = RandomizedSearchCV(rf,
                          params, 
                          scoring = 'neg_root_mean_squared_error',
                          n_jobs = -1,
                          verbose = 0,
                          cv = CV)

rf_search.fit(X_train, y_train)

rf_model = rf_search.best_estimator_
mae_rf, rmse_rf = run_model(rf_model)
print('Finished modelling :D\n')

# save the model
print('Saving the model...\n')
model = rf_model
output_file = 'model_rf.bin'

with open(output_file, 'wb') as f_out:
    pickle.dump(model, f_out)

print(f'The model was saved to "{output_file}"')