import sqlite3
import pandas as pd


def sql_query_1():
    """Sample query made on existing database, and exporting query output to dataframe"""
    connection = sqlite3.connect('files/meteors.db')
    connection.row_factory = sqlite3.Row

    first_query = "SELECT recclass,  CAST(AVG(mass) AS INT) AS Avg_Mass" \
                  " FROM meteors GROUP BY recclass" \
                  " ORDER BY Avg_Mass DESC;"

    df1 = pd.read_sql(first_query, con=connection)

    return df1


def sql_query_2():
    """Sample query made on existing database, and exporting query output to dataframe"""
    connection2 = sqlite3.connect('files/meteors.db')
    connection2.row_factory = sqlite3.Row

    second_query = "SELECT recclass,  CAST(AVG(mass) AS INT) AS Avg_Mass" \
                   " FROM meteors WHERE mass <=5000" \
                   " GROUP BY recclass" \
                   " ORDER BY Avg_Mass DESC;"

    df2 = pd.read_sql(second_query, con=connection2)

    return df2



def create_sheets(key, gc, working_spreadsheet):
    """
    Function made to extract data to brand new sheets in choosen file
    :param key: actual worksheet id (defined in console.py)
    :param gc: variable for storing credentials for service (located in files/main.py)
    :param working_spreadsheet: actual worksheet instance (defined in console.py)
    """

    df1 = sql_query_1()
    df2 = sql_query_2()

    query_1 = working_spreadsheet.add_worksheet(title='sql_query_1', rows=200, cols=6)
    query_2 = working_spreadsheet.add_worksheet(title='sql_query_2', rows=200, cols=6)

    query_1.update([df1.columns.values.tolist()] + df1.values.tolist())
    query_2.update([df2.columns.values.tolist()] + df2.values.tolist())

    return query_1, query_2



