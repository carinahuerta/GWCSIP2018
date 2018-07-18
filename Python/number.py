print ("Welcome to guess the number!")
from random import *
aRandomNumber = randint(0,10)

guess = input ("Guess a number between 0 and 10 (inclusive):")

count =0
while (count < 5 ):
    count += 1
    if (int(guess)< aRandomNumber):
        guess = input ("Guess a higher number: ")
    if (int(guess) > aRandomNumber):
        guess = input ("Guess a lower number: ")
    if (int(guess) ==aRandomNumber):
        print ("Correct!")
        break
    if (count == 5):
        print ("Better luck next time.")
        break
    if not guess.isnumeric() :
        print("That's not a positive whole number, try again!")
