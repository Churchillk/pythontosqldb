import mysql.connector
def insert_data():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'CLASSA',
    }
    
    # Sample data to be inserted
    new_member = {
        'CODE': '6',
        'FNAME': 'John',
        'LNAME': 'Doe',
        'CONTACT': '+24412345678',
        'AGE': '50',
        'GMAIL': 'john.doe@example.com'
    }
    
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        insert_query = "INSERT INTO MEMBERS (CODE, FNAME, LNAME, CONTACT, AGE, GMAIL) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (new_member['CODE'], new_member['FNAME'], new_member['LNAME'], new_member['CONTACT'], new_member['AGE'], new_member['GMAIL']))
        connection.commit()
        print("Data inserted successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
insert_data()
