
import pandas as pd

def normalize(df):
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    df["date"] = df["date"].dt.date
    df = df.groupby("date").mean().reset_index()
    return df[["date", "price"]]
