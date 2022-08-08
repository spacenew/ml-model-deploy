import os
import pickle
import argparse

import pandas as pd
from sklearn.model_selection import train_test_split


def dump_pickle(obj, filename):
    with open(filename, "wb") as f_out:
        return pickle.dump(obj, f_out)


def read_dataframe(filename: str):
    df = pd.read_csv(filename)

    categorical = df.dtypes[df.dtypes == 'object'].index.to_list()
    df[categorical] = df[categorical].astype(str)

    return df


def split_data(df: pd.DataFrame):
    print(f'Encoding data...')
    data = preprocess(df)

    X = data.drop('charges', axis=1)
    y = data['charges'].values

    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        random_state=2022)
    print(f'Data splitted...')
    return X_train, X_test, y_train, y_test


def preprocess(df: pd.DataFrame):

    df['sex'] = df['sex'].map({"female": 0, "male": 1})
    df['region'] = df['region'].map(
        {'southwest': 0, 'southeast': 1, 'northwest': 2, 'northeast': 3})
    df['smoker'] = df['smoker'].map({"yes": 1, "no": 0})

    return df


def run(raw_data_path: str, dest_path: str):
    # load csv files
    print(f'Read dataset...')
    df = read_dataframe(
        os.path.join(raw_data_path)
    )

    # split data
    print(f'Start splitting data...')
    X_train, X_test, y_train, y_test = split_data(df)

    # create dest_path folder unless it already exists
    os.makedirs(dest_path, exist_ok=True)

    # save datasets
    dump_pickle((X_train, y_train), os.path.join(dest_path, "train.pkl"))
    print(f'Save datasets train')
    dump_pickle((X_test, y_test), os.path.join(dest_path, "test.pkl"))
    print(f'Save datasets test')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--raw_data_path",
        default="./raw_data/insurance.csv",
    )
    parser.add_argument(
        "--dest_path",
        default="./preprocessed_data",
    )
    args = parser.parse_args()

    run(args.raw_data_path, args.dest_path)
