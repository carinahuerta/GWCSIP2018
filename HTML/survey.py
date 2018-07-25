def questions():
    questions_list = [
    "What is your first name?",
    "How old are you? ",
    "What type of hair lenght is best? ",
    "What is your average commute time? ",
    "What is your favorite topping on pizza? ",
    "What is your favorite color? ",
    "What type of phone is best? ",
    "What type of cereal is best? ",
    "What is your favorite thing from the cafeteria? ",
    "What is the best kind of chips? "
    ]
    keynames = ["name", "age", "hair", "commute", "pizza", "color", "phone", "cereal", "caf", "chips"]
    listofanswers = {}
    i = 0
    for i in range (len(questions_list)):
        answer= input(questions_list[i])
        listofanswers[keynames [i]]= answer

    myDict =[]
    myDict.append (listofanswers)
    print(myDict)
    fileobj = open("surveyanswers.txt", "w")
    fileobj.write(str(myDict))

questions()
