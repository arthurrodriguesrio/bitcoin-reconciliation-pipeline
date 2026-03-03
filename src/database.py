
from sqlalchemy import create_engine

def save_to_db(df, table_name="bitcoin_reconciliation"):
    engine = create_engine("sqlite:///market_data.db")
    df.to_sql(table_name, engine, if_exists="replace", index=False)
