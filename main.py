from fastapi import FastAPI
import random
from models import FoodItem, Order, Restaurant, User, category, OTPVerification
from utils import (
    savecategory,
    savefooditem,
    saveorder,
    saverestaurant,
    saveotp,
    saveuser,
    read_db,
    write_db
)

app  = FastAPI(
    title="Food delivery API",
    description="This is a sample API built with FastAPI.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Welcome to the Food Delivery API!. Here is the docs at /docs"}

@app.post("/signup")
def signup_user(name: str, email: str, password: str):
    db = read_db()

    if any(u["email"] == email for u in db["users"]):
        return {"error": "This email has already been registered"}
    
    new_user = User(name=name, email=email, password=password)
    new_user_dict = new_user.to_dict()
    new_user_dict["password"] = password

    saveuser(new_user_dict)

    # generate otp for the user
    otp_code = str(random.randint(100000, 999999))
    otp = OTPVerification(user_id=new_user.id, code=otp_code)
    saveotp(otp.to_dict())

    return {"message": "User signed up successfully. An otp has been sent to verify your email", 
            "user": new_user.to_dict(),
            "otp": otp_code
    }

@app.post("/verify-email")
def verify_email(user_id: str, code: str):
    db = read_db()
    otp_records = db.get("otps", [])

    matching_otp = next((o for o in otp_records if o["user_id"] == user_id and o["code"] == code), None)
    if not matching_otp:
        return {"error": "Invalid OTP or user ID"}
    
    for user in db["users"]:
        if user["id"] == user_id:
            user["email_verified"] = True
            break

    write_db(db)
    print(f"Verifying OTP {code} for user {user_id}")
    return {"message": "Email verified successfully"}

    
    # fetch the token from the databae that matches the suer id and the code.
    #  if there is not match, return an error message to the user
    # else verify the user's email
   

@app.post("/login")
def login_user(email: str, password: str):
    db = read_db()
    users = db.get("users", [])

    user = next((u for u in users if u["email"] == email), None)
    if not user:
        return {"error": "User not found"}
    
    if user["password"] != password:
        return {"error": "Incorrect password"}
    
    if not user.get("email_verified", False):
        return {"error": "Email not verified. Please verify the OTP. "}
    return {"message": f"User {user['name']} logged in successfully"}
    # fetch the user from the database using the email
    # if user not found, return error message
    # else check if the password matches
    # if password matches, return success message
    

