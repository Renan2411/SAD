import pandas as pd
import sqlite3

SQL_ESTRUTURA_TABELA_AIRLINES = "SELECT sql FROM sqlite_master WHERE type='table' And name='airports';"

SQL_SHOW_TABLES = "SELECT name FROM sqlite_master WHERE type='table';"

SQL_SELECT_LATITUDE_LONGITUDE = "SELECT latitude,longitude FROM airports LIMIT 5;"

SQL_ROTAS = """
    SELECT 
        cast(sa.longitude as float) as source_longitude, 
        cast(sa.latitude as float) as source_latitude, 
        cast(da.longitude as float) as dest_longitude, 
        cast(da.latitude as float) as dest_latitude 
    FROM routes 
    INNER JOIN airports sa 
        ON sa.id = routes.source_id
    INNER JOIN airports da
        ON da.id = routes.dest_id;
"""

conn = sqlite3.connect("semana0302_flights.db")
df = pd.read_sql_query(SQL_ROTAS, conn)

print(df)

conn.close()