from datetime import datetime
import os


def CreateBillDirectory():
    if not os.path.exists("./Bills"):
        os.mkdir("./Bills")


def BillGenerator(BILL_ID, DATE, BILL_TEXT):
    CreateBillDirectory()

    TIME = datetime.now().strftime("%H:%M:%S")

    TEXT = "==================================".center(100)
    TEXT += "\n" + ("Shudh Restaurant Management System".center(100))
    TEXT += "\n" + ("==================================".center(100))
    TEXT += (
        "\n\n"
        + ("Bill ID: " + str(BILL_ID)).center(50)
        + ("Date/Time: " + str(DATE) + " / " + str(TIME)).center(50)
        + "\n\n"
    )
    TEXT += BILL_TEXT
    TEXT += "\n\n" + "Thanks For Shopping, Visit Again!".center(100)

    BILL_FILE = f"./Bills/Bill_{str(BILL_ID)}_{str(DATE)}.txt"

    with open(BILL_FILE, "w", encoding="utf-8") as f:
        f.write(TEXT)
    return BILL_FILE


def GetBillText(BILL_ID, DATE):
    try:
        BILL_FILE = f"./Bills/Bill_{str(BILL_ID)}_{str(DATE)}.txt"
        with open(BILL_FILE, "r", encoding="utf-8") as f:
            BILL_TEXT = f.read()
        return BILL_FILE, BILL_TEXT
    except:
        return "", "Bill Not Found"
