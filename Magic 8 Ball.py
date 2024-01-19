#Magic 8 Ball
#Lam Manning
#Jan 19
#Initialize
import random

resp = ["Yes", "No", "My Sources say No", "Unlikely",  "Concentrate, and ask again", "Better not tell you now", "Most likely", "Ask Again Later", "Without a Doubt", "Very Doubtful"]

#function
#Asks user if they want to run the program again
def runagain():
    again = input("Do you wish to ask another question? (y)or(n): ")
    if(again=="y"):
        magic8ball()
    elif(again=="n"):
        print("See you next time.")
        quit()
    else:
        print("Please type 'y' or 'n'")
        runagain()
#Gives a random response to a user's yes or no question. The question must end with a question mark and at the end will ask if the user wants to run the program again.
def magic8ball():
    quest = input("Ask the Magic 8 ball a Yes or No question. Make sure it ends in with a question mark: ")
    if(quest.endswith("?")==False):
        print("Please place a questionmark at the end of your question")
        magic8ball()
    else:
        print("""        ____
    ,dP9CGG88@b,
  ,IP  _   Y888@@b,
 dIi  (_)   G8888@b
dCII  (_)   G8888@@b
GCCIi     ,GG8888@@@
GGCCCCCCCGGG88888@@@
GGGGCCCGGGG88888@@@@...
Y8GGGGGG8888888@@@@P.....
 Y88888888888@@@@@P......
 `Y8888888@@@@@@@P'......
    `@@@@@@@@@P'.......
        """"........""")
        print(random.choice(resp))
    runagain()
        

    
#main
magic8ball()