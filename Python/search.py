def linear():
    amt = int(input("Let's make a list. How many elements do you want in it? "))
    linlist = []
    linelem = 0
    while(linelem < amt):
        lin = int(input("Enter number: "))
        linlist.append(lin)
        linelem+=1
    linsearch = int(input("Search a number to see if it's in your list: "))
    if linsearch in linlist:
        print("Yes, " + str(linsearch) + " is in your list.\n")
        return
    else:
        print("No, " + str(linsearch) + " isn't in your list.\n")
        return


def binary():
    biamt = int(input("Let's make a list. How many elements do you want in it? "))
    bilist = []
    bielem = 0
    while(bielem < biamt):
        bi = int(input("Enter number: "))
        bilist.append(bi)
        bielem+=1
    bilist.sort()
    print(bilist)

    high = len(bilist) - 1
    low = 0
    mid = int(high/2)

    bisearch = int(input("Search a number to see if it's in your list: "))
    while(low != high):
        if bisearch == bilist[mid]:
            print("Yes, " + str(bisearch) + " is in your list.\n")
            return
        if bisearch < bilist[mid]:
            high = mid - 1
            mid = int(high/2)
        if bisearch > bilist[mid]:
            low = mid + 1
            mid = int(low + (high-low)/2)
    if bisearch != bilist[mid]:
        print("No, " + str(bisearch) + " isn't in your list.\n")
        return


def bubble():
    

def main():
    toc = input("Press: \n1 for Linear Search \n2 for Binary Search \n3 for Bubble Sort \n4 to exit \n ")
    if toc == "1":
        linear()
    elif toc == "2":
        binary()
    elif toc == "3":
        bubble()
    elif toc == "4":
        exit()
    else:
        print("That was not an option.")

main()
