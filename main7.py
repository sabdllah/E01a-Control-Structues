#!/usr/bin/env python3

import utils

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')
color = input("What is my favorite color? ")
color = color.lower().strip()
if (color == 'red'):
    print('Correct!')
elif (color == 'pink'):
    print('Close!')
else:
    print('Sorry, try again.')
    
   
print('Hello!')
color = input("What is my favorite color? ")
input ("burgundy")
color = color.lower().strip()
if (color == 'red'):
    print('Correct!')
elif (color == 'pink'):
    print('Close!')
else:
    print('Sorry, try again.') 