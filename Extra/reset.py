import mysql.connector
from Utils.SqlHandler import getMySqlPassword


# Creating database

PASSWORD = getMySqlPassword()
mydb = mysql.connector.connect(host="localhost", user="root", password=PASSWORD)
mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE restaurant_manager")
print("Database deleted")