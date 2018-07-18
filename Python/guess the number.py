i = 3
while True
    i += 1
if (i> 3)
    break
from random import *
aRandomNumber = randint(1,20)
print (aRandomNumber)
guess = input ("Guess a number between 1 and 20 (inclusive):")
if not guess.isnumeric ():
    print("That's not a positive whole number, try again!")
else:
    guess = int(guess)
