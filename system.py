import sys
from loggin import loggin
from register import register
from CLASS_User import User

logged_in = False
system_on = True
user = User(None, None)

while(system_on):
    if (logged_in):
        print('You are logged in. What\'s now?')
        cmd = input()

    else:
        print('Welcome! Choose one from below:')
        print('   Loggin           Register')
        cmd = input()

        if('LOGGIN' == cmd.upper()):
            logged_in = loggin()

            if (logged_in):
                #load user info
                x = 0

        elif('REGISTER' == cmd.upper()):
            register()

        else:
            print('Something went wrong. Please try again.')
