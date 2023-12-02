#Importing Libraries Required

import requests
import pymysql

#Importing Database Connection
from database import connection

conn =connection()
cursor=conn.cursor()
'''
#Exectuting Query
cursor.execute("show tables;")
tables=cursor.fetchall()

#Prinitng Data in Loop
for table in tables:
    print(table)
'''
'''
def create_user(username, password):
    try:
        conn = connection()
        with conn.cursor() as cursor:
            if username == 'sami' and password == 'sami@1234':
                # Insert into Wallet table
                cursor.execute("INSERT INTO Wallet (Walletid) VALUES (2);")
                # Insert into Users table
                cursor.execute("INSERT INTO Users (Userid, Walletid) VALUES (2, 2);")
                # Commit the changes

                return 1
                conn.commit()
    except pymysql.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection in the finally block
        if cursor:
            cursor.close()
        if conn:
            conn.close()
'''
# Call the function
def username(username,password):
    if username =='sami' and password =='sami1234':
        return 1
    else:
        return 0

def tablefill(a):
    try:
        conn = connection()

        cursor.execute("INSERT INTO Wallet (Walletid) VALUES (1);")
    # Insert into Users table
        cursor.execute("INSERT INTO Users (Userid, Walletid) VALUES (1, 1);")
        conn.commit()
    except pymysql.Error as e:
        print(f"Error: {e}")

