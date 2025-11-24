import json
from pathlib import Path

DB_FILE = Path("db.json")


def read_db():
    if not DB_FILE.exists():
        return {"users": [], "otps":[]}
    with open(DB_FILE, "r") as f:
        return json.load(f)
    
def write_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def saveuser(user_dict):
    db = read_db()
    db["users"].append(user_dict)
    write_db(db)
    print("user saved:", user_dict)
    
def saveotp(otp):
    db = read_db()
    db["otps"].append(otp)
    write_db(db)
    print("OTP saved:", otp)

def savecategory(category):
    print("Saving category:", category)
def savefooditem(food_item):
    print("Saving food item:", food_item)
def saverestaurant(restaurant):
    print("Saving restaurant:", restaurant)
def saveorder(order):
    print("Saving order:", order)