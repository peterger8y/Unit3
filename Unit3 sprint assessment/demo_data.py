import sqlite3
import pandas as pd

list1 = ["s", "x", "y"]
list2 = [["g", 3, 9], ["v", 5, 7], ["f", 8, 7]]
df = pd.DataFrame(columns=list1, data=list2)

conn = sqlite3.connect("demo_data.sqlite3")
curs = conn.cursor()

prequery = "DROP TABLE IF EXISTS demo"
curs.execute(prequery)
conn.commit()

create_table_query = "CREATE TABLE IF " \
                     "NOT EXISTS demo(s varchar(1), x int, y int);"
curs.execute(create_table_query)
conn.commit()

for row in df.iterrows():
    query1 = """insert into demo ({})
values ({})
    """.format(
        ", ".join(list1), "'" + "', '".join([str(x) for x in row[1]]) + "'"
    )
    curs.execute(query1)
    conn.commit()

query = "SELECT COUNT(*) FROM demo"
curs.execute(query)
row_count = curs.fetchall()
# [(3,)]
query2 = "SELECT COUNT(*) FROM demo WHERE x>=5 and y>=5"
curs.execute(query2)
xy_at_least_5 = curs.fetchall()
# [(2,)]
query_3 = "SELECT COUNT(DISTINCT(y)) FROM demo"
curs.execute(query_3)
unique_y = curs.fetchall()
# [(2,)]
