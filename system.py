import sys
from loggin import loggin
from loggin import user
from register import register
from CLASS_User import User
from save import save
from update_user_info import update_user_info


logged_in = False
system_on = True

while(system_on):
    if (logged_in):
        if (user.get_firstName() == 'unknown'):
            print('\nWelcome back, ' + user.get_username())
        else:
            print('\nWelcome back, ' + user.get_firstName())

        print(' Info    Update      SingOut     Quit')
        cmd = input(user.get_username() + '@home:')

        if('INFO' == cmd.upper()):
            user.print()

        elif('UPDATE' == cmd.upper()):
            update_user_info(user)
            save(user)

        elif('SINGOUT' == cmd.upper()):
            save(user)
            del user
            user = User(None, None)
            logged_in = False

        elif('QUIT' == cmd.upper()):
            save(user)
            sys.exit()

    else:
        print('Welcome! Choose one from below:')
        print('Loggin    Register    Quit')
        cmd = input('~:')

        if('LOGGIN' == cmd.upper()):
            logged_in = loggin(user)


        elif('REGISTER' == cmd.upper()):
            register()

        elif('QUIT' == cmd.upper()):
            sys.exit()


        else:
            print('Something went wrong. Please try again.')
