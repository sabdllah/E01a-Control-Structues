#!/usr/bin/env python3

import utils

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')
color = input("What is my favorite color? ")
if (color == 'Red' or color == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')
    color = input ('burgundy')
    if (color == 'BurdGundy' or color = 'burgUndy'):
    print ('Correct!')
    else:
        print ('Sorry, try again.')