def moderator_menu(user):
    MOD_MENU = True
    while(MOD_MENU):
        print('********Moderator panel********')
        print('  Test     Help      Back    ')
        cmd = input(user.get_username() + '@mod:')

        if('TEST' == cmd.upper()):
            print('TESTING COMMAND WORKS FINE')

        elif('HELP' == cmd.upper()):
            print('***MODERATOR COMMANDS***' +
                '\nTEST - does nothing. For texting purpose' +
                '\nHELP - Shows all moderator commands' +
                '\nBACK - goes back to main page')

        elif('BACK' == cmd.upper()):
            print('Exiting moderatro panel')
            MOD_MENU = False
