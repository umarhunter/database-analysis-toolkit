import pandas as pd
from rapidfuzz import fuzz, process


def perform_fuzzy_matching(df, columns, threshold=90):
    """
    Perform fuzzy matching on specified columns of a DataFrame.

    @param df: pandas DataFrame containing the data.
    @param columns: List of columns to perform fuzzy matching on.
    @param threshold: Matching threshold (0-100), where a higher number indicates a stricter match.
    return: DataFrame with potential matches.
    """
    # Create a result DataFrame to store the matches
    result_df = pd.DataFrame(columns=["index1", "index2", "match_score"] + columns)

    # Iterate through each column specified for fuzzy matching
    for column in columns:
        # Extract the column data as a list
        choices = df[column].tolist()

        # Iterate through each element in the column
        for i, item in enumerate(choices):
            # Find matches within the list
            matches = process.extract(item, choices, scorer=fuzz.ratio, limit=None)

            # Filter matches by threshold and avoid self-matching
            for match in matches:
                match_index = match[2]
                match_score = match[1]

                if match_score >= threshold and match_index != i:
                    # Append the matches to the result DataFrame
                    result_df = result_df.append({
                        "index1": i,
                        "index2": match_index,
                        "match_score": match_score,
                        column: item,
                        f"{column}_match": choices[match_index]
                    }, ignore_index=True)

    return result_df
