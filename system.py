import sys
from loggin import loggin
from register import register

print('Welcome! Choose one from below:')
print('   Loggin           Register')
cmd = input()

if('LOGGIN' == cmd.upper()):
    loggin()

elif('REGISTER' == cmd.upper()):
    register()

else:
    print('Wrong input. Please try again later')
    sys.exit()
