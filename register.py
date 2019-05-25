import os
from userExists import userExists

def checkUsername(username):
    for i in username:
        for j in '\#\\"£!$%^&*()_+|~/?;\'\ ':
            if (i == j):
                print('Username has invalid characters')
                return True

    return False

def register():
    username_VALID = True
    while (username_VALID):
        username = input('Username: ')
        password = input('Password: ')
        username_VALID = checkUsername(username)

    if(userExists(username)):
        print('Username already taken. Try other one.')
        register()

    else:
        f = open('users/' + username, 'w')
        f.write(password)
