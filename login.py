import os
from getpass import getpass
from userExists import userExists
from register import register
from CLASS_User import User

user = User(None, None)

def loadUser(user, username, password):
    user.set_username(username)
    user.set_password(password)
    f = open('users/' + username, 'r')
    for textLine in f:
        if 'firstName=' in textLine: user.set_firstName(textLine[10:].rstrip())
        elif 'lastName=' in textLine: user.set_lastName(textLine[9:].rstrip())
        elif 'email=' in textLine: user.set_email(textLine[6:].rstrip())
        elif 'age=' in textLine: user.set_age(int(textLine[4:].rstrip()))
        elif 'gender=' in textLine: user.set_gender(textLine[7:].rstrip())
        elif 'admin=' in textLine: user.set_admin(int(textLine[6:].rstrip()))
        elif 'moderator=' in textLine: user.set_moderator(int(textLine[10:].rstrip()))

    f.close()

def login(user):
    print('')
    username = input('Username: ')
    password = getpass('Password: ')

    if (userExists(username)):
        f = open('users/' + username, 'r')
        textLine = f.readline()
        if(textLine[9:].rstrip() == password):
            loadUser(user, username, password)
            f.close()
            return True
        else:
            print('Password is incorrect')
            f.close()
            return False

    else:
        print('User does not exist. Do you want to register? [y/n]')
        cmd = input()

        if ('Y' == cmd.upper()):
            register()

        else:
            return False
