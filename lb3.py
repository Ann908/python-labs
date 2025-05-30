import hashlib
import sqlite3

connection = sqlite3.connect('first_database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users_table (
id INTEGER PRIMARY KEY,
login TEXT NOT NULL,
password TEXT NOT NULL,
full_name TEXT NOT NULL)''')

def hash_pass(password):
    return hashlib.sha256(password.encode()).hexdigest()

def insert_users():
    while True:
        login = input('What is your username? ')
        cursor.execute('SELECT * FROM Users_table WHERE login = ?', (login,))
        if cursor.fetchone():
            print("This username already exists. Please choose another one.")
        else:
            break

    password = hash_pass(input('What is your password? '))
    full_name = input('What is your full name? ')
    cursor.execute('INSERT INTO Users_table (login, password, full_name) VALUES (?, ?, ?)', (login, password, full_name))
    connection.commit()
    print("User is inserted.")

def update_password():
    login = input("What login, which password you want to change? ")
    password = hash_pass(input('What is your new password? '))
    cursor.execute('UPDATE Users_table SET password = ? WHERE login = ?', (password, login))
    connection.commit()
    print("Password updated.")


def authenticate_user():
    login = input('Enter your login: ')
    password = hash_pass(input('Enter your password: '))

    cursor.execute('SELECT password FROM Users_table WHERE login = ?', (login,))
    row = cursor.fetchone()

    if row is None:
        print('Username does not exist.')
        return

    print("Your username is correct!")

    if password == row[0]:
        print("Password is correct!")
    else:
        print("Password is wrong!")
        password_new = input("Please, input password again: ")
        hashed_new_password = hash_pass(password_new)
        if hashed_new_password == row[0]:
            print("Password is correct!")
        else:
            print("You don't have any attempts!")

if __name__ == '__main__':
    while True:
        insert_users()
        update_password()
        authenticate_user()


connection.commit()
connection.close()