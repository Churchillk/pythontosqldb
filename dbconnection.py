import mysql.connector

def getdb():
    db_config = {
        'host': 'enter your host name',
        'user': 'enter your username',
        'password': 'enter your password',
        'database': 'enter your database name',
    }
    
    try:
        connection = mysql.connector.connect(**db_config)
        print("CONNECTION SUCCESSFULL")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    cursor = connection.cursor()
    cursor.execute("write any custom sql code")
    results = cursor.fetchall()
    for row in results:
        print(row)
        
    cursor.close()
    connection.close()


if __name__ == "__main__":
    getdb()