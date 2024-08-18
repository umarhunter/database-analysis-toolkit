# Utility file (util.py)
import os


def get_features(data):
    return data.columns.tolist()


def save_csv(df, filename, file_type='.csv'):
    directory = 'results/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = directory + filename + file_type
    df.to_csv(file_path, index=False)


def save_excel(df, filename):
    directory = 'results/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, filename + '.xlsx')
    df.to_excel(file_path, index=False)


def save_json(df, filename):
    directory = 'results/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, filename + '.json')
    df.to_json(file_path, orient='records', lines=True)


def save_parquet(df, filename):
    directory = 'results/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, filename + '.parquet')
    df.to_parquet(file_path, index=False)


def save_feather(df, filename):
    directory = 'results/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, filename + '.feather')
    df.to_feather(file_path)
