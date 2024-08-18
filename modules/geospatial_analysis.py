# geospatial_analysis.py
import pandas as pd
from haversine import haversine, Unit


def perform_geospatial_analysis(df, sort_cols, geo_cols, threshold):
    """
    Perform geospatial analysis on specified columns of a DataFrame.

    @param df: pandas DataFrame containing the data.
    @param sort_cols: List of columns to sort by before performing geospatial analysis.
    @param geo_cols: List of two columns representing latitude and longitude.
    @param threshold: Distance threshold in kilometers to consider rows as a match.
    @return: DataFrame with rows that are within the distance threshold.
    """
    # Sort the DataFrame based on the sort columns
    df = df.sort_values(by=sort_cols).reset_index(drop=True)

    # Create a list to store the results
    results = []

    # Group the DataFrame by the sort columns
    grouped_df = df.groupby(sort_cols)

    for group_name, group in grouped_df:
        lat_col, lon_col = geo_cols

        # Extract the latitude and longitude as tuples
        coords = list(zip(group[lat_col], group[lon_col]))

        for i, coord1 in enumerate(coords):
            for j in range(i + 1, len(coords)):
                coord2 = coords[j]

                # Calculate the Haversine distance between the two coordinates
                distance = haversine(coord1, coord2, unit=Unit.KILOMETERS)

                if distance <= threshold:
                    # Collect rows that are within the threshold
                    results.append({
                        "index1": group.index[i],
                        "index2": group.index[j],
                        "distance_km": distance,
                        lat_col: coord1[0],
                        lon_col: coord1[1],
                        f"{lat_col}_match": coord2[0],
                        f"{lon_col}_match": coord2[1]
                    })

    # Convert the list of dictionaries to a DataFrame
    result_df = pd.DataFrame(results)

    return result_df
