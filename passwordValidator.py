import re
while True:

    password = input('enter the password you want to validate: ')

    if len(password) < 8:
        print('password too short')
        break
    else:
        if not re.search('[A-Z]', password):
            print('password must contain an uppercase letter')
            break
        if not re.search('[a-z]', password):
            print('password must contain a lowercase letter')
            break
        if not re.search('[0-9]', password):
            print('password must contain digits')
            break
        if not re.search('[@_!#$%^&*()<>?/\|}{~:]', password):
            print('password must contain special characters')
            break
    print('password is valid')
