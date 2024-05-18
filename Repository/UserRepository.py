import json
from Model.User import User

def check_user_existence(username):
    with open("Database/Entity/users.json", "r") as file:
        users = json.load(file)
        for user in users:
            if user["username"] == username:
                return True
            
    return False

def get_all_users():
    users = []
    with open("Database/Entity/users.json", "r") as file:
        data = json.load(file)
        for i in data:
            user = User(i["id"], i["username"], i["password"], i["carbon_footprint"])
            users.append(user)

    return users

def add_user(username, password):
    with open("Database/Entity/users.json", "r") as file:
        users = json.load(file)
        user_id = len(users) + 1
        new_user = {
            "id": user_id,
            "username": username,
            "password": password,
            "carbon_footprint": 0
        }
        users.append(new_user)
        
    with open("Database/Entity/users.json", "w") as file:
        json.dump(users, file, indent=4)
    
    user_obj = User(user_id, username, password, 0)
    
    return user_obj