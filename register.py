import os
from userExists import userExists
from CLASS_User import User
from save import save

def checkUsername(username):
    for i in username:
        for j in '\#\\"£!$%^&*()_+|~/?;\'\ ':
            if (i == j):
                print('Username has invalid characters')
                return True

    return False

def register():
    username_INVALID = True
    while (username_INVALID):
        print('')
        username = input('Username: ')
        password = input('Password: ')
        username_INVALID = checkUsername(username)

    if(userExists(username)):
        print('Username already taken. Try other one.')
        register()

    else:
        user = User(username, password)
        print('\nPlease enter information below')
        print('If you do not want to answer, just input 0')
        user.ask()
        save(user)

        del user
        print('You are now registered! Please log in')
