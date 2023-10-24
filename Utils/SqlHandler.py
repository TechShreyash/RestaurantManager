import datetime
import os
import mysql.connector


# Get MySql Password
def getMySqlPassword():
    if os.path.isfile("./extra/password.txt"):
        with open("./extra/password.txt", "r") as f:
            PASSWORD = f.read()
    else:
        PASSWORD = ""

    if PASSWORD == "":
        PASSWORD = input("Enter MySql Password: ")
        with open("password.txt", "w") as f:
            f.write(PASSWORD)
            print("Password saved to password.txt")

    return PASSWORD


# Connect to MySql

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=getMySqlPassword(),
    database="restaurant_manager",
)
mycursor = mydb.cursor(buffered=True)


# Add Dish
def AddDishToDB(name, price):
    name = name.title()
    mycursor.execute("INSERT INTO dishes (name, price) VALUES (%s, %s)", (name, price))
    mydb.commit()


# Update Dish
def UpdateDishInDB(name, price):
    name = name.title()
    mycursor.execute(
        "UPDATE dishes SET price = %s WHERE name = %s",
        (price, name),
    )
    mydb.commit()


# Get Dishes
def GetDishesFromDB():
    mycursor.execute("SELECT * FROM dishes")
    dishes = mycursor.fetchall()
    return dishes


# Delete Dish
def DeleteDishFromDB(name):
    name = name.title()
    mycursor.execute("DELETE FROM dishes WHERE name = %s", (name,))
    mydb.commit()


# Save Order
def SaveOrderInDB(PRICE):
    try:
        mycursor.execute("SELECT * FROM orders")
        ID = len(mycursor.fetchall()) + 1
    except:
        ID = 1

    DATE = datetime.datetime.date(datetime.datetime.now())
    mycursor.execute(
        "INSERT INTO orders (id,price,date) VALUES (%s,%s,%s)", (ID, PRICE, DATE)
    )
    mydb.commit()
    return ID, DATE


# Get Orders
def GetOrdersFromDB():
    mycursor.execute("SELECT * FROM orders")
    orders = mycursor.fetchall()
    return orders
