import pandas as pd
import sqlite3

try:
    conn = sqlite3.connect('cinema.db')
except Error as e:
    print(e)

#Show all table names
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(f"Table Name : {cursor.fetchall()}\n")

print("-----USERS-----")
df = pd.read_sql_query('SELECT * FROM user', conn)
print(df)
print()

print("-----STATES-----")
df = pd.read_sql_query('SELECT * FROM state', conn)
print(df)
print()

print("-----CITIES-----")
df = pd.read_sql_query('SELECT * FROM city', conn)
print(df)
print()

conn.close()