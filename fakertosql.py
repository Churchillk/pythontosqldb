from faker import Faker
import mysql.connector
import random
from time import sleep

db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'NERDS',
    }
data = []
def generate_random_data(num_entries=10):
    fake = Faker()

    value = 0
    for _ in range(num_entries):
        code = value
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        contact = fake.phone_number()
        age = random.randint(1, 50)

        new_member = {
            'CODE': code,
            'FNAME': first_name,
            'LNAME': last_name,
            'CONTACT': contact,
            'AGE': age,
            'EMAIL': email
        }
        try:
            connection = mysql.connector.connect(**db_config)
            print("connection established")
            cursor = connection.cursor()
            insert_query = "INSERT INTO `NERD MEMBERS` (CODE, FNAME, LNAME, CONTACT, AGE, EMAIL) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (new_member['CODE'], new_member['FNAME'], new_member['LNAME'], new_member['CONTACT'], new_member['AGE'], new_member['EMAIL']))
            connection.commit()
            
        except mysql.connector.Error as err:
            print(f"DB-CONNECTION Error: {err}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        value += 1
        sleep(1)
        print(f"inserted {code}, {first_name}, {last_name}, {contact}, {age}, {email}")
    print("Data inserted successfully!")
    
if __name__ == "__main__":
    random_data = generate_random_data(50)
