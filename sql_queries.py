import gspread
import sqlite3
import pandas as pd
from main import key


def sql_query_1():
    connection = sqlite3.connect('meteors.db')
    connection.row_factory = sqlite3.Row

    first_query = "SELECT recclass,  CAST(AVG(mass) AS INT) AS Avg_Mass" \
                  " FROM meteors GROUP BY recclass" \
                  " ORDER BY Avg_Mass DESC;"

    df1 = pd.read_sql(first_query, con=connection)

    return df1


def sql_query_2():
    connection2 = sqlite3.connect('meteors.db')
    connection2.row_factory = sqlite3.Row

    second_query = "SELECT recclass,  CAST(AVG(mass) AS INT) AS Avg_Mass" \
                   " FROM meteors WHERE mass <=5000" \
                   " GROUP BY recclass" \
                   " ORDER BY Avg_Mass DESC;"

    df2 = pd.read_sql(second_query, con=connection2)

    return df2



def create_sheets():

    df1 = sql_query_1()
    df2 = sql_query_2()

    gc = gspread.service_account(filename='meteors_client_secret.json')
    sh = gc.open_by_key(key)

    query_1 = sh.add_worksheet(title='sql_query_1', rows=200, cols=6)
    query_2 = sh.add_worksheet(title='sql_query_2', rows=200, cols=6)

    query_1.update([df1.columns.values.tolist()] + df1.values.tolist())
    query_2.update([df2.columns.values.tolist()] + df2.values.tolist())

    return query_1, query_2


create_sheets()
