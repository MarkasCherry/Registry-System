import os
from userExists import userExists
from register import register

def loggin():
    print('')
    username = input('Username: ')
    password = input('Password: ')

    if (userExists(username)):
        f = open('users/' + username, 'r')
        for textLine in f:
            if 'password=' in
            return True

        else:
            print('Password is incorrect')
            return False

    else:
        print('User does not exist. Do you want to register? [y/n]')
        cmd = input()

        if ('Y' == cmd.upper()):
            register()

        else:
            return False
