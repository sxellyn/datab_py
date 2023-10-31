import sqlite3

sqlite3.connect("testing.db")

def create_db(database_name:str):
    """_summary_

    Args:
        database_name (str): _description_
    """
    sqlite3.connect(database_name)