import os

def userExists(username):
    users = os.listdir('users/')
    for user in users:
        if (user == username):
            return True

    else:
        return False
