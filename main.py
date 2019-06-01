import sys
from login import login
from login import user
from register import register
from CLASS_User import User
from save import save
from update_user_info import update_user_info
from moderator_menu import moderator_menu
from admin_menu import admin_menu

logged_in = False
system_on = True

MENU_MESSAGE = ' Info    Update    SingOut    '

while(system_on):
    if (logged_in):
        if (user.get_firstName() == 'unknown'):
            print('\nWelcome back, ' + user.get_username())
        else:
            print('\nWelcome back, ' + user.get_firstName())

        if(user.get_admin() == 1): print(MENU_MESSAGE + 'Moderate    Administrate')
        elif(user.get_moderator() == 1): print(MENU_MESSAGE + 'Moderate')
        else: print(' Info    Update    SingOut')
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

        elif('MODERATE' == cmd.upper()):
            if(user.get_moderator() == 1 or user.get_admin() == 1): moderator_menu(user)
            else: print('You do not have privilages')

        elif('ADMINISTRATE' == cmd.upper()):
            if(user.get_admin() == 1): admin_menu(user
            else: print('You do not have privilages')

    else:
        print('Welcome! Choose one from below:')
        print('Login    Register    Quit')
        cmd = input('~:')

        if('LOGIN' == cmd.upper()):
            logged_in = login(user)


        elif('REGISTER' == cmd.upper()):
            register()

        elif('QUIT' == cmd.upper()):
            sys.exit()


        else:
            print('Something went wrong. Please try again.')
