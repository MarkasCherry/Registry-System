def admin_menu(user):
    ADMIN_MENU = True
    while(ADMIN_MENU):
        print('********ADMIN panel********')
        print('  Test     Help      Back    ')
        cmd = input(user.get_username() + '@mod:')

        if('TEST' == cmd.upper()):
            print('TESTING COMMAND WORKS FINE')

        elif('HELP' == cmd.upper()):
            print('***ADMIN COMMANDS***' +
                '\nTEST - does nothing. For texting purpose' +
                '\nHELP - Shows all admin commands' +
                '\nBACK - goes back to main page')

        elif('BACK' == cmd.upper()):
            print('Exiting admin panel')
            ADMIN_MENU = False
