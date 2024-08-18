# Utility file (util.py)

def get_features(data):
    return data.columns.tolist()


def save_csv(df, output_file):
    df.to_csv(output_file, index=False)