import pandas as pd
import sqlite3

db_path = r"./coin.db"
con = sqlite3.connect(db_path, isolation_level=None)

reader_df = pd.read_sql("SELECT * FROM 'BTC'", con, index_col="index")

print(reader_df)
