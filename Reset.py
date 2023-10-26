import mysql.connector
import os

# Get MySql Password
if os.path.isfile("password.txt"):
    with open("password.txt", "r") as f:
        PASSWORD = f.read()
else:
    PASSWORD = ""

if PASSWORD == "":
    PASSWORD = input("Enter MySql Password: ")
    with open("password.txt", "w") as f:
        f.write(PASSWORD)
        print("Password saved to password.txt")

# Creating database

mydb = mysql.connector.connect(host="localhost", user="root", password=PASSWORD)
mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE restaurant_manager")
print("Database deleted")
