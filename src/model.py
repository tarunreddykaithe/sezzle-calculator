import sqlite3
from sqlite3 import Error
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

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
        logger.error("Unable to connect to Sqlite. Error is: "+str(e))

    return conn

def create_calculations_table():
    """
    This method drops if there is a table and creates a new calculations table with created_at and message columns.
    """
    con = create_connection(DATABASE)
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS calculations")
    cur.execute("CREATE TABLE calculations(operation_id INTEGER PRIMARY KEY AUTOINCREMENT, operation text NOT NULL)")
    con.commit()

def store_operation(row):
    """
    Stores operation in calculations table
    """
    try: 
        con = create_connection(DATABASE)
        cur = con.cursor()
        cur.execute(f"INSERT INTO calculations (operation) VALUES (?)",(row.get('operation'),))
        con.commit()
    except Error as e:
        logger.error("Unable to add operations to  table. Error is: "+str(e))

def list_operations():
    """
    Retreives last 10 operations of calculations table.
    """
    con = create_connection(DATABASE)
    try:
        cur = con.cursor()
        cur.execute("select operation from calculations order by operation_id desc limit 10")
        rows = cur.fetchall()
        result=[]
        for row in rows:
            result.append({
                'operation':row[0]
                } )
        return result
    except Error as e:
        logger.error("Unable to retrive operations from Sqlite. Error is: "+str(e))