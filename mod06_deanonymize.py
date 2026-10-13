import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """

    list_pairs = []

    for anon in anon_df.itertuples():
        found_match = dict()
        found = False
        dup = False
        for aux in aux_df.itertuples():
            if (aux.age == anon.age) and (aux.zip3 == anon.zip3) and (aux.gender == anon.gender):
                if found == True:
                    dup = True
                    break
                    
                found_match["anon_id"] = anon.anon_id
                found_match["matched_name"] = aux.name
                found = True
        if found == True and dup == False:
            list_pairs.append([found_match["anon_id"], found_match["matched_name"]])

    df = pd.DataFrame(list_pairs, columns=["anon_id", "matched_name"])
    return df
    # raise NotImplementedError


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """

    return matches_df.shape[0] / anon_df.shape[0]
    # raise NotImplementedError




# For testing purposes

# anon_path = "anonymized.csv"
# aux_path = "auxiliary.csv"

# anon, aux = load_data(anon_path, aux_path)

# matches = link_records(anon, aux)

# print(matches)
