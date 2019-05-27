import sys
from loggin import loggin
from loggin import user
from register import register
from CLASS_User import User
from save import save


logged_in = False
system_on = True

while(system_on):
    if (logged_in):
        if (user.get_firstName() == 'unknown'):
            print('Welcome back, ' + user.get_username())
        else:
            print('Welcome back, ' + user.get_firstName())

        print(' Quit    SingOut')
        cmd = input()

        if('SINGOUT' == cmd.upper()):
            save(user)
            del user
            user = User(None, None)
            logged_in = False

        if('QUIT' == cmd.upper()):
            save(user)
            sys.exit()

    else:
        print('Welcome! Choose one from below:')
        print('   Loggin           Register')
        cmd = input()

        if('LOGGIN' == cmd.upper()):
            logged_in = loggin(user)


        elif('REGISTER' == cmd.upper()):
            register()

        else:
            print('Something went wrong. Please try again.')
