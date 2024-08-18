import pandas as pd
from rapidfuzz import fuzz, process, utils


def perform_fuzzy_matching(df, sort_cols, fuz_cols, threshold=90):
    """
    Perform fuzzy matching on specified columns of a DataFrame.

    @param df: pandas DataFrame containing the data.
    @param sort_cols: List of columns to sort and group by before performing matching.
    @param fuz_cols: List of columns to perform fuzzy matching on.
    @param threshold: Matching threshold (0-100), where a higher number indicates a stricter match.
    return: DataFrame with potential matches.
    """
    # Sort the DataFrame based on the sort columns. Sorting before grouping is important for performance,
    # and allows us to visualize the rows.
    df = df.sort_values(by=sort_cols).reset_index(drop=True)

    # Create a list to store dictionaries of matches
    results = []

    # Group the DataFrame by the sort columns
    grouped_df = df.groupby(sort_cols)

    for group_name, group in grouped_df:
        for col in fuz_cols:
            choices = group[col].tolist()

            for index, item in enumerate(choices):
                # Compare the current item against the rest of the group
                for j in range(index + 1, len(choices)):
                    match_score = fuzz.WRatio(item, choices[j], processor=utils.default_process)

                    if match_score >= threshold:
                        # Collect the match result as a dictionary
                        results.append({
                            "index1": group.index[index],
                            "index2": group.index[j],
                            "match_score": match_score,
                            col: item,
                            f"{col}_match": choices[j]
                        })

    # Convert the list of dictionaries to a DataFrame
    result_df = pd.DataFrame(results)

    return result_df
