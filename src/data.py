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
    cur.execute("CREATE TABLE calculations(operation_id INTEGER PRIMARY KEY AUTOINCREMENT, operation text NOT NULL)")
    con.commit()

def insert(result):
    try: 
        con = create_connection(DATABASE)
        cur = con.cursor()
        cur.execute(f"INSERT INTO calculations (operation) VALUES (?)",(result.get('operation'),))
        con.commit()
    except Error as e:
        print(e)

def select_all_calculations():
    con = create_connection(DATABASE)
    try:
        cur = con.cursor()
        cur.execute("select operation from calculations order by operation_id desc limit 10")
        rows = cur.fetchall()
        result = [{'operation':row[0]} for row in rows ]
        return result
    except Error as e:
        print(e)