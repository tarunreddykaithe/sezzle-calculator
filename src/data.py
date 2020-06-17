import sqlite3
from sqlite3 import Error

DATABASE = 'solutions.db'


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table():
    """
    create table with created_at and message columns
    """
    con = create_connection(DATABASE)
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS calculations")
    cur.execute("CREATE TABLE calculations(transaction_id INTEGER PRIMARY KEY AUTOINCREMENT, message text NOT NULL)")
    con.commit()

def insert(result):
    
    con = create_connection(DATABASE)
    cur = con.cursor()
    cur.execute("INSERT INTO calculations (message) VALUES (?)", (result,))
    con.commit()

def select_all_calculations():
    con = create_connection(DATABASE)
    cur = con.cursor()
    cur.execute("select message from calculations order by transaction_id desc limit 10")
    rows = cur.fetchall()
    return rows
