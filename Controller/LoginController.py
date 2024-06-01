from Repository.UserRepository import check_user_existence, get_all_users, add_user, change_password_by_id, get_password_by_id

def login_success(username, password):
    for user in get_all_users():
        if user.username == username and user.password == password:
            return True, user
            
    return False, None
    
def register_user(username, password, home_country):
    if check_user_existence(username):
        return False, None

    user = add_user(username, password, home_country)
        
    return True, user

def change_password(user_id, new_password):
    change_password_by_id(user_id, new_password)

def get_password(user_id):
    return get_password_by_id(user_id)