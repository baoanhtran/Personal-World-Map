from Repository.UserRepository import check_user_existence, get_all_users, add_user, change_password_by_id, get_password_by_id

def login_success(username, password):
    if username == "" or password == "":
        return False, None, "Please type all fields"
    
    for user in get_all_users():
        if user.username == username and user.password == password:
            return True, user, ""
        
    return False, None, "Wrong username or password"

def register_user(username, password):
    if username == "" or password == "":
        return False, None, "Please type all fields"
    
    if check_user_existence(username):
        return False, None, "This username is already taken"
    
    user = add_user(username, password)

    return True, user, ""

def change_password(user_id, new_password, password_confirmation):
    if new_password == "" or password_confirmation == "":
        return False, "Please type all fields"
    
    if new_password != password_confirmation:
        return False, "Passwords do not match"
    
    if new_password == get_password_by_id(user_id):
        return False, "New password is the same as the old one"
    
    change_password_by_id(user_id, new_password)
    
    return True, ""