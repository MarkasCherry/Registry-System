class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.firstName = 'unknown'
        self.lastName = 'unknown'
        self.email = 'unknown'
        self.age = 0
        self.gender = 'unknown'
        self.admin = 0
        self.moderator = 0

    #setters
    def set_password(self, password):
        self.password = password

    def set_firstName(self, firstName):
        self.firstName = firstName

    def set_lastName(self, lastName):
        self.lastName = lastName

    def set_email(self, email):
        self.email = email

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    def set_admin(self, admin):
        self.admin = admin

    def set_moderator(self, moderator):
        self.moderator = moderator

    #getters
    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_firstName(self):
        return self.firstName

    def get_lastName(self):
        return self.lastName

    def get_email(self):
        return self.email

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_admin(self):
        return self.admin

    def get_moderator(self):
        return self.moderator

    #ask for input
    def ask_password(self):
        data = input('Enter your old password: ')
        if(data == self.password):
            data = input('Enter new password: ')
            self.set_password(data)

        else:
            print('Wrong password.')

    def ask_firstName(self):
        data = input('Your first name: ')
        if (data == '0'): data = 'unknown'
        self.set_firstName(data)

    def ask_lastName(self):
        data = input('Your last name: ')
        if (data == '0'): data = 'unknown'
        self.set_lastName(data)

    def ask_email(self):
        data = input('Your email address: ')
        if (data == '0'): data = 'unknown'
        self.set_email(data)

    def ask_age(self):
        data = input('Your your age: ')
        self.set_age(data)

    def ask_gender(self):
        data = input('Your sex: ')
        if (data == '0'): data = 'unknown'
        self.set_age(data)

    def ask(self):
        self.ask_firstName()
        self.ask_lastName()
        self.ask_email()
        self.ask_age()
        self.ask_gender()
