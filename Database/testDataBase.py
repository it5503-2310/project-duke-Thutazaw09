import sqlite3

def empty_table(tableName:str)-> None:
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('mainDataBase.db')
        # Create a cursor object to execute SQL commands
        cursor = conn.cursor()
        # Define the SQL statement to delete all rows from the table
        delete_query = f"DELETE FROM {tableName};"
        # Execute the SQL query to delete all rows
        cursor.execute(delete_query)
        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        print(f"All data removed from table '{tableName}' successfully.")
    except sqlite3.Error as e:
        print(f"Error emptying table '{tableName}': {e}")


# Establish the Connection with Database
con = sqlite3.connect("mainDataBase.db")
cur = con.cursor()

t1 = str({"id" : 2,"done" : False,"type" : "event","title" : "Meeting","start_time" : "2pm","end_time" : "4pm"})

dataToInsert = (t1,)

insert_query = "INSERT INTO Storage (task) VALUES (?);"


cur.execute(insert_query,dataToInsert)
result = cur.execute("""SELECT * from Storage;""")


while row :=  result.fetchall():
    print(row)
    
    
print("Clear database")
empty_table("Storage")

result = cur.execute("""SELECT * from Storage;""")
while row :=  result.fetchall():
    print(row)
  






