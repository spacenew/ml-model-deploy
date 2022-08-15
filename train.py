import os
import pickle

import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

from hyperopt import STATUS_OK, Trials, fmin, hp, tpe
from hyperopt.pyll import scope


def load_pickle(filename):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


def train_model_search(X_train, y_train, X_test, y_test, num_trials=100):
    def objective(params):
        regr = RandomForestRegressor(**params)
        rf = regr.fit(X_train, y_train)

        y_pred = rf.predict(X_test)
        rmse = mean_squared_error(y_test, y_pred, squared=False)

        return {'loss': rmse, 'status': STATUS_OK}

    search_space = {
        'max_depth': scope.int(hp.quniform('max_depth', 1, 20, 1)),
        'n_estimators': scope.int(hp.quniform('n_estimators', 10, 50, 1)),
        'min_samples_split': scope.int(
            hp.quniform('min_samples_split', 2, 10, 1)),
        'min_samples_leaf': scope.int(
            hp.quniform('min_samples_leaf', 1, 4, 1)),
        'random_state': 2022
    }

    rstate = np.random.default_rng(2022)

    best_result = fmin(
        fn=objective,
        space=search_space,
        algo=tpe.suggest,
        max_evals=num_trials,
        trials=Trials(),
        rstate=rstate
    )

    return best_result


def train_best_model(X_train, y_train, X_test, y_test):
    best_params = {
        'max_depth': 4,
        'n_estimators': 24,
        'min_samples_split': 3,
        'min_samples_leaf': 4,
        'random_state': 2022
    }

    regr = RandomForestRegressor(**best_params)
    rf = regr.fit(X_train, y_train)

    y_pred = rf.predict(X_test)

    mean_squared_error(y_test, y_pred, squared=False)

    with open("models/best_rf_model.b", "wb") as f_out:
        pickle.dump(rf, f_out)


def main(data_path: str = "./preprocessed_data"):
    X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
    X_test, y_test = load_pickle(os.path.join(data_path, "test.pkl"))
    train_model_search(X_train, y_train, X_test, y_test)
    train_best_model(X_train, y_train, X_test, y_test)


if __name__ == '__main__':
    main()
