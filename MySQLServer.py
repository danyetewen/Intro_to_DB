#!/usr/bin/python3
"""
MySQLServer.py
A simple script to create the database 'alx_book_store' in MySQL server.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (update user/password if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        # replace with your MySQL username
            password="password" # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database (won't fail if it already exists)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: Unable to connect or create database -> {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection closed.")   # optional

if __name__ == "__main__":
    create_database()

