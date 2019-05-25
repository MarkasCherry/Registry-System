import os
from userExists import userExists
from register import register

def loggin():
    username = input('Username: ')
    password = input('Password: ')

    if (userExists(username)):
        f = open('users/' + username, 'r')
        if(f.readline() == password):
            print('Successful')

        else:
            print('Password is incorrect')
            loggin()

    else:
        print('User does not exist. Do you want to register? [y/n]')
        cmd = input()

        if ('Y' == cmd.upper()):
            register()
