import sqlite3
from typing import Any

def createTable(tableName:str, dataBaseName:str):
    try:
        conn = sqlite3.connect(dataBaseName)
        cursor = conn.cursor()
        createTableQuery = f'''
        CREATE TABLE IF NOT EXISTS New{tableName} (
            roll_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT
        );
        '''
        cursor.execute(createTableQuery)
        print(f"Create Table '{tableName}' Successfully")
    except sqlite3.Error as e:
        print(e)

def deleteTable(tableName:str,dataBaseName:str)-> None:
    try:
        conn = sqlite3.connect(dataBaseName)
        cursor = conn.cursor()
        deleteQuery = f"DROP TABLE IF EXISTS {tableName};"
        cursor.execute(deleteQuery)
        conn.commit()
        conn.close()
        print(f"Table '{tableName}' deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting table '{tableName}': {e}")
         
def emptyTable(tableName:str,dataBaseName:str)-> None:
    try:
        con = sqlite3.connect(dataBaseName)
        cur = con.cursor()
        deleteQuery = f"DELETE FROM {tableName};"
        cur.execute(deleteQuery)
        con.commit()
        con.close()
        print(f"All data removed from table '{tableName}' successfully.")
    except sqlite3.Error as e:
        print(f"Error emptying table '{tableName}': {e}")
  
def addToTable(tableName:str,dataBaseName:str,data:str) -> None:
    try:
        con = sqlite3.connect(dataBaseName)
        cur = con.cursor()
        insertQuery = f"INSERT INTO {tableName} (task) VALUES (?);"
        dataToInsert = (data,)
        cur.execute(insertQuery,dataToInsert)
        con.commit()
        con.close()
        print(f"Data Added Successfully to the table {tableName}")
    except sqlite3.Error as e:
        print(f"Error Addition to table tasks: {e}")
        
def lookUpTable(tableName:str,dataBaseName:str) -> None:
    try:
        con = sqlite3.connect(dataBaseName)
        cur = con.cursor()
        lookUpQuery = f"SELECT * FROM {tableName};"
        result = cur.execute(lookUpQuery)
        print("Showing Data")
        while row := result.fetchall():
            print(row)
            
        con.commit()
        con.close()
        
    except sqlite3.Error as e:
        print(f"Error Looking Up table tasks: {e}")
    
    
tableName = "tasks"
dataBaseName = "taskDataBase.db"


# clear the table
emptyTable(tableName,dataBaseName)

# add item to table
t1 = str({"id" : 1,"done" : False,"type" : "event","title" : "Meeting","start_time" : "2pm","end_time" : "4pm"})
addToTable(tableName,dataBaseName,t1)

# looking up
lookUpTable(tableName,dataBaseName)

