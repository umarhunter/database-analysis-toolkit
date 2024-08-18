import pandas as pd


def load_data(input_file):
    if input_file.endswith('.csv'):
        return pd.read_csv(input_file)

    # Add support for other file formats
    # Caution: anything other than CSV may require additional dependencies, I will not test this code
    elif input_file.endswith('.xlsx'):
        return pd.read_excel(input_file)
    elif input_file.endswith('.json'):
        return pd.read_json(input_file)
    elif input_file.endswith('.parquet'):
        return pd.read_parquet(input_file)
    elif input_file.endswith('.feather'):
        return pd.read_feather(input_file)
    else:
        raise ValueError("Invalid file format. Please provide a valid file format.")
