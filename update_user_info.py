def update_user_info(user):
    print('\nChoose what you want to update:')
    print('1. Password' +
        '\n2. First name' +
        '\n3. Second name' +
        '\n4. Email address' +
        '\n5. Age' +
        '\n6. Gender' +
        '\n0. To cancel')

    cmd = input(user.get_username() + '@profile:')

    if('1' == cmd):
        user.ask_password()
        print('Your password has been updated!')

    elif('2' == cmd):
        user.ask_firstName()
        print('Your first name has been updated!')


    elif('3' == cmd):
        user.ask_lastName()
        print('Your last name has been updated!')

    elif('4' == cmd):
        user.ask_email()
        print('Your email address has been updated!')

    elif('5' == cmd):
        user.ask_age()
        print('Your age has been updated!')

    elif('6' == cmd):
        user.ask_gender()
        print('Your gender has been updated!')

    else:
        print('Profile has not been updated')
