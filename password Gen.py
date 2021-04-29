import random

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+|/?><'

while True:
    password_length = int(
        input('what length would you like your password to be: '))
    NumberOfPassword = int(
        input('how many passwords would you like to generate at once: '))
    if password_length < 8:
        password_length = 8
    for x in range(0, NumberOfPassword):
        password = ''
        for x in range(0, password_length):
            password_character = random.choice(characters)
            password += password_character
        print('here is your password: ', password)
