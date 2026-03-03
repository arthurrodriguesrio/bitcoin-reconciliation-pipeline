
import requests
import pandas as pd

def get_bitcoin_prices(days=30):
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    prices = data["prices"]

    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    return df
