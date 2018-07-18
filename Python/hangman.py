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
