#Importing Libraries Required

import requests
import pymysql
from datetime import datetime
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


#Username and Password Function, brought from Firebase
def username(username,password):
    if username =='sami' and password =='sami1234':
        return 1
    else:
        return 0

#FIll table according.
def tablefill():
    try:
        conn = connection()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO Wallet (Walletid) VALUES (1);")
    # Insert into Users table
        cursor.execute("INSERT INTO Users (Userid, Walletid) VALUES (1, 1);")
        conn.commit()
    except pymysql.Error as e:
        print(f"Error: {e}")

def enteramount():
    # Get the amount as input
    amount_str = input("Enter Amount you want to Deposit: ")


    try:
        amount = float(amount_str)
    except ValueError:
        print("Invalid amount. Please enter a valid numeric value.")
        return

    # Get the current date and time
    current_datetime = datetime.now()

    # Establish a database connection
    try:
        conn = connection()
        cursor = conn.cursor()

        # Update the total amount in the Wallet table
        cursor.execute(f"UPDATE Wallet SET totalamount = {amount} WHERE Walletid = 1;")

        #  datetime as a string in 'YYYY-MM-DD HH:MM:SS' format
        formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

        # Insert a transaction record
        cursor.execute(f"INSERT INTO transactions (walletid, amount, transactiontime) VALUES (1, {amount}, '{formatted_datetime}');")

        # Commit the changes
        conn.commit()

        print("Transaction completed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:

        if cursor:
            cursor.close()
        if conn:
            conn.close()


us=input("Enter Username : ")
ps=input("Enter Password : ")
if username(us,ps):
    print("Correct Username")
    #tablefill()
    enteramount()
else:
    print("Wrong Password")
