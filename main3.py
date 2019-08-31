#!/usr/bin/env python3

import utils

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')
print('Hello!')
color = input("What is my favorite color? ")
color = input ('Burdguny')
if (color == 'Red'):
    print('Correct!')
else:
    print('Sorry, try again.')