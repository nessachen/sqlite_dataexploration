import pandas as pd
import sqlite3

conn = sqlite3.connect('healthcare.db')

df = pd.read_csv('leading_deaths.csv')

df.to_sql('death_causes', conn, if_exists = 'replace', index = False)

query1 = " SELECT * FROM death_causes WHERE [Cause Name] = 'Kidney disease' "
result1_df = pd.read_sql(query1, conn)
print(result1_df)

query2 = " SELECT COUNT(*) AS death_count FROM death_causes WHERE Deaths > 100 "
result2_df = pd.read_sql(query2, conn)
print(result2_df)

query3 = " SELECT [Cause Name], AVG(Deaths) AS avg_deaths FROM death_causes GROUP BY [Cause Name] "
result3_df = pd.read_sql(query3, conn)
print(result3_df)

query4 = " SELECT [Age-adjusted Death Rate], [Cause Name] FROM death_causes ORDER BY [Age-adjusted Death Rate] LIMIT 10 "
result4_df = pd.read_sql(query4, conn)
print(result4_df)
