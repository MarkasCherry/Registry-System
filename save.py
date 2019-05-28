import os

def save(user):
    f = open('users/' + user.get_username(), 'w').close()
    f = open('users/' + user.get_username(), 'w')
    f.write('password=' + user.get_password() +
            '\nusername=' + user.get_username() +
            '\nfirstName=' + user.get_firstName() +
            '\nlastName=' + user.get_lastName() +
            '\nemail=' + user.get_email() +
            '\nage='+ str(user.get_age()) +
            '\ngender=' + user.get_gender() +
            '\nadmin=' + str(user.get_admin()) +
            '\nmoderator=' + str(user.get_moderator()))
    f.close()
