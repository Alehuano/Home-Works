import sqlite3

from db import cursor, connection


def initiate_db():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
        ''')

    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?,?,?)',
                       (f'Продукт{i}', f'Описание{i}', i * 100))

    connection.commit()
    connection.close()


def add_user(username, email, age):
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()

    cursor.execute(f'INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)',
                   (username, email, age, 1000))
    connection.commit()


def is_included(username):
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()

    check_user = cursor.execute('SELECT * FROM Users WHERE username=?', (username,))
    if check_user.fetchone() is None:
        return False
    else:
        return True


def get_all_products():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.commit()
    return products
