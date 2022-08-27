from typing import Counter


orjinal_password = 6143
reverse_password = 3416
Counter= 1
while Counter < 4:
    password = int (input('please enter your password : '))
    if orjinal_password == password:
        print ('Wellcom.')
        break
    elif  reverse_password == password:
        print ('calling the police.')
        break
    elif Counter == 3:
        print ('your account has been blocked!')
        break
    else:
        print('try again.')
        Counter += 1
