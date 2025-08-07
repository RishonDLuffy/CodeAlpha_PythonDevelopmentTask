#Simple Rule based chat bot
#By Rishon D'souza

#Various possible variable

hello = ["hi", "hello", "hey", "yo"]
howAreYou = ["how are you", "how r u", "how are you doing", "how's it going"]
imGoodToo=["im good","i am good","good too"]
askName = ["what is your name", "who are you", "your name","name","what are you"]
whoMadeYou = ["who made you", "who created you", "who built you"]
goodbye = ["bye", "goodbye", "see you", "later", "cya"]
help=["help","assistance"]


while True:
    userStatement=input("User:")
    if userStatement.lower() in hello:
        print("RishonBot:Hello there!")
    elif userStatement.lower() in howAreYou:
        print("RishonBot:I'm Good, What about you?")
    elif userStatement.lower() in imGoodToo:
        print("RishonBot:Thats great to hear!")
    elif userStatement.lower() in askName:
        print("RishonBot:My Name is RishonBot,I'm a Simple Chatbot.")
    elif userStatement.lower() in whoMadeYou:
        print("RishonBot:I was made by Rishon, an intern.")
    elif userStatement.lower() in goodbye:
        print("RishonBot:Goodbye!")
        break
    elif userStatement.lower() in help:
        print("RishonBot:You can ask somthing along the lines of:" \
        "hello,how are you,whats your name,who made you and finally a goodbye to exit the conversation.")
    else:
        print("I dont understand, type 'help' for available instructions.")
