from Repository.UserRepository import check_user_existence, get_all_users, add_user

def login_success(username, password):
    for user in get_all_users():
        if user.username == username and user.password == password:
            return True, user
            
    return False, None
    
def register_user(username, password):
    if check_user_existence(username):
        return False, None

    user = add_user(username, password)
        
    return True, user