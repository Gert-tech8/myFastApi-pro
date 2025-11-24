import uuid 

class User():
    def __init__(self, name: str, email: str, password: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.password = password
        self.email_verified = False  # In a real application, ensure to hash the password

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "email_verified": self.email_verified
        }

class OTPVerification():
    def __init__(self, user_id: str, code: str):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.code = code

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "code": self.code
        }

class category:
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.name = name

class FoodItem():
    def __init__(self, name: str, description: str, price: float, category_id: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price
        self.category_id = category_id

class Restaurant():
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.profile_image = None

class Order():
    def __init__(self, user_id: str, food_item_ids: list):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.food_item_ids = food_item_ids
        self.restaurant_id = None