import pandas as pd
from rapidfuzz import fuzz, utils
from sentence_transformers import SentenceTransformer, util as sbert_util

# Load the pre-trained model (this can take some time initially)
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')


def perform_fuzzy_matching(df, sort_cols, fuz_cols, threshold=90, algorithm="WRatio"):
    """
    Perform fuzzy matching on specified columns of a DataFrame.

    @param df: pandas DataFrame containing the data.
    @param sort_cols: List of columns to sort and group by before performing matching.
    @param fuz_cols: List of columns to perform fuzzy matching on.
    @param threshold: Matching threshold (0-100), where a higher number indicates a stricter match.
    @param algorithm: The fuzzy matching algorithm to use (e.g., WRatio, ratio, partial_ratio, token_sort_ratio, semantic).
    return: DataFrame with potential matches.
    """
    algorithm_map = {
        "WRatio": fuzz.WRatio,
        "ratio": fuzz.ratio,
        "partial_ratio": fuzz.partial_ratio,
        "token_sort_ratio": fuzz.token_sort_ratio,
        "semantic": None  # Placeholder for semantic matching
    }

    results = []
    df = df.sort_values(by=sort_cols).reset_index(drop=True)
    grouped_df = df.groupby(sort_cols)

    for group_name, group in grouped_df:
        for col in fuz_cols:
            choices = group[col].tolist()

            if algorithm == "semantic":
                # Compute embeddings for the entire list of choices
                embeddings = model.encode(choices, convert_to_tensor=True)
                cosine_scores = sbert_util.pytorch_cos_sim(embeddings, embeddings)

                for i in range(len(choices)):
                    for j in range(i + 1, len(choices)):
                        match_score = cosine_scores[i][j].item() * 100
                        if match_score >= threshold:
                            results.append({
                                "index1": group.index[i],
                                "index2": group.index[j],
                                "match_score": match_score,
                                col: choices[i],
                                f"{col}_match": choices[j]
                            })
            else:
                fuzz_function = algorithm_map.get(algorithm, fuzz.WRatio)
                for index, item in enumerate(choices):
                    for j in range(index + 1, len(choices)):
                        match_score = fuzz_function(item, choices[j], processor=utils.default_process)
                        if match_score >= threshold:
                            results.append({
                                "index1": group.index[index],
                                "index2": group.index[j],
                                "match_score": match_score,
                                col: item,
                                f"{col}_match": choices[j]
                            })

    result_df = pd.DataFrame(results)
    return result_df
