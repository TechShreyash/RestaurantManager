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

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=PASSWORD,
    database="restaurant_manager",
)

mycursor = mydb.cursor()

DISHES = [
    ("Dosa", 125),
    ("Butter Chicken", 220),
    ("Palak Paneer", 200),
    ("Chana Masala", 180),
    ("Aloo Gobi", 190),
    ("Samosa", 100),
    ("Naan", 50),
    ("Tandoori Chicken", 250),
    ("Biryani", 280),
    ("Rogan Josh", 220),
    ("Dahi Bhalla", 90),
    ("Idli", 100),
    ("Tandoori Aloo", 180),
    ("Raita", 60),
    ("Pav Bhaji", 140),
]


for dish in DISHES:
    try:
        mycursor.execute("INSERT INTO dishes (name, price) VALUES (%s, %s)", dish)
    except Exception as e:
        print(e)
        print(f"Failed to insert {dish}")

mydb.commit()
print("Successfully inserted dishes")
