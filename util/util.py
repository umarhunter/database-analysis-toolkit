# Utility file (util.py)
import logging
import os


def get_features(data):
    return data.columns.tolist()


def save_file(df, filename):
    # Extract the file extension
    filename_without_ext, file_extension = os.path.splitext(filename)
    logging.info(f"Attempting to write file with extension: {file_extension}")

    # Determine the correct save function to use based on the file extension
    if file_extension == '.csv':
        save_csv(df, filename_without_ext)  # Remove the extension before passing it because the helper functions add it
    elif file_extension == '.xlsx':
        save_excel(df, filename_without_ext)
    elif file_extension == '.json':
        save_json(df, filename_without_ext)
    elif file_extension == '.parquet':
        save_parquet(df, filename_without_ext)
    elif file_extension == '.feather':
        save_feather(df, filename_without_ext)
    else:
        raise ValueError(
            "Unsupported file extension. Please use one of the following: .csv, .xlsx, .json, .parquet, .feather")


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
