print ("You are a shark named Dom and you come across Liam the fish while swimming home.")
startgame = input ("Are you 'friends' or 'enemies'?")

if (startgame == 'friends'):
    print ("Liam says, 'God I missed you!'")
    print ("'I missed you too,' you say.")
    pastfuture = input ("Should they talk about 'past' or 'future'?")
    if (pastfuture == 'past'):
        print ("Remember when we went to Johnny's house and got trashed?")
        print ("Liam says, 'Yeah, then his parents caught us. Those were some good times...'")
    if (pastfuture == 'future'):
        print("Liam gazes into your eyes. 'Before I met you, my heart grew to lie in the shadows. You brought me into the light with your shining smile. You're always in my mind. Even when I'm asleep, my closed eyes are desperately waiting for the sight of you. I cannot exist without you, for I am forgetful of anything but seeing you again. Without you, I would be nothing. You se something in me that gives my heart a reason to beat. Dom, I love you. I love you BECAUSE I love you, because it would be impossible for me not to love you. My chest aches with love for you; my body aches for your touch. I look into your eyes and I see my future. You are my everything, Dom, and I love you. Will you marry me?")
        marriage = input('yes' or 'no')
        if(marriage == 'yes'):
            print("They lived happily ever after.")
        if(marriage == 'no'):
            print("You died alone.")
if(startgame == 'enemies'):
    print("'I ate your girl's plankton last night, if y'know what I mean,' Liam mutters. You eat him.")
