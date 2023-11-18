import mysql.connector

# Replace these values with your MySQL server details
host = '54.152.118.196'
user = 'sami'
password ='Thepassword@1234'
database = 'sami'

try:
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    print("Databases:")
    for db in databases:
        print(db[0])

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()


