from Utils.BillHandler import GetBillText
from Utils.SqlHandler import (
    AddDishToDB,
    DeleteDishFromDB,
    GetDishesFromDB,
    GetOrdersFromDB,
    UpdateDishInDB,
)

# Menu for Admin


def showMenu():
    print()
    print("==================================".center(100))
    print("Shudh Restaurant Management System".center(100))
    print("==================================".center(100))
    print()
    print("ADMIN MENU".center(100))
    print()
    print(" " * 25 + "1. Add New Dish")
    print(" " * 25 + "2. Update Dish")
    print(" " * 25 + "3. Show Dishes")
    print(" " * 25 + "4. Delete Dish")
    print(" " * 25 + "5. Show Orders")
    print(" " * 25 + "6. Show Bills")
    print(" " * 25 + "7. Show Income")
    print(" " * 25 + "0. Exit")
    print()

    choice = int(input(">> Enter your choice: "))
    if choice == 1:
        addDish()
    elif choice == 2:
        updateDish()
    elif choice == 3:
        showDishes()
    elif choice == 4:
        deleteDish()
    elif choice == 5:
        showOrders()
    elif choice == 6:
        showBills()
    elif choice == 7:
        showIncome()
    elif choice == 0:
        print()
        print("Exiting...")
        exit()
    else:
        print("Invalid Choice")
        print()
        input("Press Enter To Open Menu...")

    showMenu()


# Fucntions for Admin Menu


def addDish():
    print()
    print("============".center(100))
    print("Add New Dish".center(100))
    print("============".center(100))
    print()
    NAME = input("Enter Dish Name: ")
    PRICE = int(input("Enter Dish Price: "))
    AddDishToDB(NAME, PRICE)
    print()
    print(">> Dish Added Successfully")
    print()
    input("Press Enter To Open Menu...")


def updateDish():
    print()
    print("===========".center(100))
    print("Update Dish".center(100))
    print("===========".center(100))
    print()
    NAME = input("Enter Dish Name: ")
    PRICE = int(input("Enter Dish Price: "))
    UpdateDishInDB(NAME, PRICE)
    print()
    print(">> Dish Updated Successfully")
    print()
    input("Press Enter To Open Menu...")


def showDishes():
    print()
    print("================".center(100))
    print("Available Dishes".center(100))
    print("================".center(100))
    print()

    print("=" * 100)
    print("|| ID ||" + "DISH".center(50) + "||" + "PRICE".center(38) + "||")
    print("=" * 100)

    DISHES = GetDishesFromDB()
    pos = 1
    for dish, price in DISHES:
        print(
            "||"
            + str(pos).center(4)
            + "||"
            + dish.title().center(50)
            + "||"
            + (str(price) + " ₹").center(38)
            + "||"
        )
        pos += 1
    print("=" * 100)

    print()
    input("Press Enter To Open Menu...")


def deleteDish():
    print()
    print("===========".center(100))
    print("Delete Dish".center(100))
    print("===========".center(100))
    print()
    NAME = input("Enter Dish Name: ")
    DeleteDishFromDB(NAME)
    print()
    print(">> Dish Deleted Successfully")
    print()
    input("Press Enter To Open Menu...")


def showOrders():
    print()
    print("===========".center(100))
    print("All Orders".center(100))
    print("===========".center(100))
    print()

    ORDERS = GetOrdersFromDB()

    print("=" * 100)
    print("|| ID ||" + "TOTAL PRICE".center(50) + "||" + "DATE".center(38) + "||")
    print("=" * 100)

    for ID, PRICE, DATE in ORDERS:
        print(
            "||"
            + str(ID).center(4)
            + "||"
            + (str(PRICE) + " ₹").center(50)
            + "||"
            + str(DATE).center(38)
            + "||"
        )
    print("=" * 100)

    print()
    input("Press Enter To Open Menu...")


def showBills():
    print()
    print("=========================".center(100))
    print("Select Order To View Bill".center(100))
    print("=========================".center(100))
    print()

    ORDERS = GetOrdersFromDB()

    print("=" * 100)
    print("|| ID ||" + "TOTAL PRICE".center(50) + "||" + "DATE".center(38) + "||")
    print("=" * 100)

    IDS = []
    for ID, PRICE, DATE in ORDERS:
        IDS.append(ID)
        print(
            "||"
            + str(ID).center(4)
            + "||"
            + (str(PRICE) + " ₹").center(50)
            + "||"
            + str(DATE).center(38)
            + "||"
        )
    print("=" * 100)

    print()

    while True:
        try:
            ORDER_ID = int(input(">> Enter Order ID: "))
            print()
        except:
            print("Invalid Order ID")
            print()
            continue

        if ORDER_ID in IDS:
            break
        else:
            print("Invalid Order ID")
            print()
            continue

    BILL_FILE, BILL_TEXT = GetBillText(ORDER_ID, ORDERS[IDS.index(ORDER_ID)][2])
    print(f"Opening Bill File: {BILL_FILE}\n")
    print(BILL_TEXT)
    print()
    input("Press Enter To Open Menu...")


def showIncome():
    ORDERS = GetOrdersFromDB()
    TOTAL = 0
    for ID, PRICE, DATE in ORDERS:
        TOTAL += PRICE

    print()
    print(f">> Total Income: {TOTAL} ₹")
    print()
    input("Press Enter To Open Menu...")


# Start The Program
if __name__ == "__main__":
    while True:
        try:
            showMenu()
        except KeyboardInterrupt:
            print()
            print("Exiting...")
            exit()
        except Exception as e:
            print("Error:", e)
            print()
            input("Press Enter To Open Menu...")
