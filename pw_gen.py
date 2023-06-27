# generates an 8 character password with option to regenerate

import secrets
import string

char = string.ascii_letters
digits = string.digits
sp_char = string.punctuation
alpha_num = char + digits + sp_char
pw_length = 8

while True:
    user_input = input('generate new password? (y/n): ')
    if user_input == 'y' or user_input == 'n':
        break
    else:
        print('y or n only')

while user_input == 'y':
    pw = ''
    for i in range(pw_length):
        pw += secrets.choice(alpha_num)

    print('password is: ' + pw)

    while True:
        user_input = input('generate new password? (y/n): ')
        if user_input == 'y' or user_input == 'n':
            break
        else:
            print('y or n only')

print('goodbye')
