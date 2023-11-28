import mysql.connector

# Replace these values with your MySQL server details
'''host = '18.205.31.181'
user = 'sami1'
password = 'Sami@1234'
database = 'sami'
'''
def connection():
 host = '3.85.167.11'
 user = 'sami1'
 password = 'Sami@1234'
 database = 'Investio'


 try:
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
    )

    return  conn.is_connected()


        # Your database operations go here

 except mysql.connector.Error as err:
    print(f"Error: {err}")

if connection():
    print("Connected")
else:
    print("Error")