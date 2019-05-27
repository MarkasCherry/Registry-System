import os
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
        if 'lastName=' in textLine: user.set_lastName(textLine[9:].rstrip())
        if 'email=' in textLine: user.set_email(textLine[6:].rstrip())
        if 'age=' in textLine: user.set_age(textLine[4:].rstrip())
        if 'age=' in textLine: user.set_age(textLine[4:].rstrip())
        if 'gender=' in textLine: user.set_gender(textLine[7:0].rstrip())
        if 'admin=' in textLine: user.set_admin(textLine[6:0].rstrip())
        if 'moderator=' in textLine: user.set_moderator(textLine[10:0].rstrip())

    f.close()


def loggin(user):
    print('')
    username = input('Username: ')
    password = input('Password: ')

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
