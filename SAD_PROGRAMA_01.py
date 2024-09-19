import sqlite3

conn = sqlite3.connect("semana0302_flights.db")

cur = conn.cursor()

SQL_ESTRUTURA_TABELA_AIRLINES = "SELECT sql FROM sqlite_master WHERE type='table' And name='airports';"

SQL_SHOW_TABLES = "SELECT name FROM sqlite_master WHERE type='table';"

SQL_SELECT_LATITUDE_LONGITUDE = "SELECT latitude,longitude FROM airports LIMIT 5;"

cur.execute(SQL_SELECT_LATITUDE_LONGITUDE)

# result = cur.fetchall()
for linha in cur.fetchall():
    print(linha)

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
    
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, lat_ts=20, resolution='c')

m.drawcoastlines()
m.drawmapboundary()

cur.close()
conn.close()