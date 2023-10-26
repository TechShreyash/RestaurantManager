from Utils.BillHandler import BillGenerator, GetBillText
from Utils.SqlHandler import GetDishesFromDB, GetOrdersFromDB, SaveOrderInDB


def showMenu():
    print()
    print("==================================".center(100))
    print("Shudh Restaurant Management System".center(100))
    print("==================================".center(100))
    print()
    print("USER MENU".center(100))
    print()
    print(" " * 25 + "1. Show Dishes")
    print(" " * 25 + "2. Order Dish")
    print(" " * 25 + "3. Show Orders")
    print(" " * 25 + "4. Show Bills")
    print(" " * 25 + "0. Exit")
    print()

    choice = int(input(">> Enter your choice: "))
    if choice == 1:
        showDishes()
    elif choice == 2:
        orderDish()
    elif choice == 3:
        showOrders()
    elif choice == 4:
        showBills()
    elif choice == 0:
        exit()
    else:
        print("Invalid Choice")

    showMenu()


# Fucntions for User Menu


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


def orderDish():
    # Showing Available Dishes

    print()
    print("============".center(100))
    print("Order Dishes".center(100))
    print("============".center(100))
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
    print("Enter ID of Dish And Quantity, Enter 0 to stop")
    print()

    ORDERS = []
    IDS_ADDED = []

    while True:
        ID = int(input(">> Enter Dish ID: "))
        if ID == 0:
            break
        if ID > (pos - 1):
            print("Invalid ID")
            print()
            continue
        if ID in IDS_ADDED:
            print("Dish Already Added")
            print()
            continue

        QUANTITY = int(input(">> Enter Dish Quantity: "))
        DISH = DISHES[ID - 1][0]
        ORDERS.append((ID, DISH, QUANTITY))
        IDS_ADDED.append(ID)
        print()

    # Showing Selected Dishes

    print()
    print("===============".center(100))
    print("Selected Dishes".center(100))
    print("===============".center(100))
    print()

    BILL_TEXT = ""
    BILL_TEXT += "=" * 100
    BILL_TEXT += (
        "\n|| ID ||"
        + "DISH".center(50)
        + "||"
        + "QUANTITY".center(18)
        + "||"
        + "PRICE".center(18)
        + "||\n"
    )
    BILL_TEXT += ("=" * 100) + "\n"

    pos = 1
    TOTAL_PRICE = 0
    for ID, DISH, QUANTITY in ORDERS:
        price = DISHES[ID - 1][1] * QUANTITY
        TOTAL_PRICE += price
        BILL_TEXT += (
            "||"
            + str(pos).center(4)
            + "||"
            + DISH.title().center(50)
            + "||"
            + str(QUANTITY).center(18)
            + "||"
            + (str(price) + " ₹").center(18)
            + "||\n"
        )
        pos += 1
    BILL_TEXT += "=" * 100
    BILL_TEXT += (
        "\n||"
        + "TOTAL PRICE =>".center(76)
        + "||"
        + (str(TOTAL_PRICE) + " ₹").center(18)
        + "||\n"
    )
    BILL_TEXT += "=" * 100
    print(BILL_TEXT)
    print()

    choice = input(">> Do you want to confirm order (Y/N): ")
    print()

    if choice == "Y" or choice == "y":
        # Saving Order to DB
        print("Order Confirmed, Bill Amount: " + str(TOTAL_PRICE) + " ₹")

        BILL_ID, DATE = SaveOrderInDB(TOTAL_PRICE)
        BILL_FILE = BillGenerator(BILL_ID, DATE, BILL_TEXT)
        print(f"Bill saved at {BILL_FILE}")
        print()
        input("Press Enter To Open Menu...")
    else:
        print("Order Cancelled")
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
