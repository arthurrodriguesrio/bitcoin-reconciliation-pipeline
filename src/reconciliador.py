
def simulate_second_source(df):
    df2 = df.copy()
    df2["price"] = df2["price"] * 1.0005  # pequena variação simulada
    return df2

def reconcile(df1, df2):
    merged = df1.merge(df2, on="date", suffixes=("_source1", "_source2"))

    merged["price_diff"] = merged["price_source1"] - merged["price_source2"]
    merged["abs_diff"] = merged["price_diff"].abs()

    return merged
