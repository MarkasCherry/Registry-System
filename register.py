import os
from getpass import getpass
from userExists import userExists
from CLASS_User import User
from save import save

def checkPassword(password):
    if(len(password) < 6):
        print('\nPassword has to be atleast 6 characters long')
        return True

    return False

def checkUsername(username):
    for i in username:
        for j in '\#\\"£!$%^&*()_+|~/?;\'\ ':
            if (i == j):
                print('Username has invalid characters')
                return True

    return False

def register():
    username_INVALID = True
    password_INVALID = True
    while (username_INVALID and password_INVALID):
        print('')
        username = input('Username: ')
        password = getpass('Password: ')
        username_INVALID = checkUsername(username)
        password_INVALID = checkPassword(password)

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
        print('\nYou are now registered! Please log in')
