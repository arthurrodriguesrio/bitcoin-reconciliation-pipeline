
import pandas as pd

def calculate_returns(df):
    df = df.sort_values("date")
    df["return"] = df["price"].pct_change()
    return df
