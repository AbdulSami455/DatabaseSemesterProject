import mysql.connector

# Replace these values with your MySQL server details
'''host = '18.205.31.181'
user = 'sami1'
password = 'Sami@1234'
database = 'sami'
'''
def connectionstatus():
 host = '54.147.159.248'
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

def connection():
    host = '54.147.159.248'
    user = 'sami1'
    password = 'Sami@1234'
    database = 'Investio'
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
    )
    return conn

