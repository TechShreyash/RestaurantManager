import mysql.connector
import os


# Get MySql Password
if os.path.isfile("Extra/password.txt"):
    with open("Extra/password.txt", "r") as f:
        PASSWORD = f.read()
else:
    PASSWORD = ""

if PASSWORD == "":
    PASSWORD = input("Enter MySql Password: ")
    with open("Extra/password.txt", "w") as f:
        f.write(PASSWORD)
        print("Password saved to Extra/password.txt")


# Creating database

mydb = mysql.connector.connect(host="localhost", user="root", password=PASSWORD)
mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE restaurant_manager")
except Exception as e:
    print(e)
    print("Failed to create database")


# Running database setup commands

mydb = mysql.connector.connect(
    host="localhost", user="root", password=PASSWORD, database="restaurant_manager"
)
mycursor = mydb.cursor()

SETUP_CMDS = [
    "CREATE TABLE dishes(name varchar(20),price int)",
    "CREATE TABLE orders(id int,price int,date date)",
]

for cmd in SETUP_CMDS:
    try:
        mycursor.execute(cmd)
    except Exception as e:
        print(e)
        print("Failed to create table")

print("Database setup complete")
