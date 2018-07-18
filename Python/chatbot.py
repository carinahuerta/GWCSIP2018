from random import *
def intro1():
    print ("Hello I am Chatbot, CB for short.")
intro1 ()
def say_hello ():
    print ("Hi " + name)
name = input ("What is your name?")
say_hello ()

answer = input ("Would you like to play a game, hear a joke, or do a math problem? ")

def process_input():
    if answer == "play a game":
        game = input ("Would you like to play 'hangman' or 'guess the number'?")
        if game == "hangman":
            print("welcome to hangman")
            word1= input ("enter word to guess: ")
            secretword = []
            secretword.extend (word1)
            list =[]
            n = 0
            while (n < len(word1)):
                list.append("_")
                n += 1
            print(list)
            maxtries = 7
            tries = 0
            while tries < maxtries:
                guess = input ("Guess a leter: ")
                for i in range (len(word1)):
                    if guess == secretword [i]:
                        list [i] = guess
                print (list)
        if game == "guess the number":
            print ("Welcome to guess the number!")
            #from random import *
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
    if answer == "hear a joke":
        joke = input ("What did the flag do to the passing people?")
        if joke == "what":
            print ("Nothing, it just waved.")
    if answer == "do a math problem":
        num1 = input("Enter num1: ")
        num2 = input("Enter num2: ")
        result = sum (int(num1), int(num2))
        print ("Sum=", result)
    if answer == "nothing":
            print ("Aw okay, bye")
def sum (num1, num2):
    return num1 + num2
process_input ()
