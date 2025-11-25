import json
from pathlib import Path

DB_FILE = Path("db.json")


def read_db():
    if not DB_FILE.exists():
        return {"users": [], 
                "otps":[],
                "categories": [],
                "food_items":[], 
                "restaurants":[], 
                "orders": []
                }
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

def savecategory(category_dict):
    db = read_db()
    db.setdefault("categories", []).append(category_dict)
    write_db(db)
    print("Category saved:", category_dict)


def savefooditem(food_item_dict):
    db = read_db()
    db.setdefault("food_items", []).append(food_item_dict)
    write_db(db)
    print("Food item saved:", food_item_dict)


def saverestaurant(restaurant_dict):
    db = read_db()
    db.setdefault("restaurants", []).append(restaurant_dict)
    write_db(db)
    print("Restaurant saved:", restaurant_dict)


def saveorder(order_dict):
    db = read_db()
    db.setdefault("orders", []).append(order_dict)
    write_db(db)
    print("Order saved:", order_dict)
