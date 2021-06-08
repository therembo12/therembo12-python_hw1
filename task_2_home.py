class WrongPassword(Exception):
    pass

try:
    correctPassword = 12345
    password = int(input('Enter password: '))
    if password == correctPassword:
        print('Current Balance \n Take cash\n Exit')
    else:
        raise WrongPassword() 

except ValueError as e:
    print(e)
except WrongPassword:
    print('Wrong Password')