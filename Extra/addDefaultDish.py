import mysql.connector
from Utils.SqlHandler import getMySqlPassword

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=getMySqlPassword(),
    database="restaurant_manager",
)
mycursor = mydb.cursor()

DISHES = [
    ("Dosa", 125),
    ("French Fries", 106),
    ("Sandwich", 175),
    ("Burger", 72),
]

for dish in DISHES:
    try:
        mycursor.execute(
            "INSERT INTO dishes (name, price) VALUES (%s, %s)", dish
        )
    except Exception as e:
        print(e)
        print(f"Failed to insert {dish}")

mydb.commit()
print("Successfully inserted dishes")
