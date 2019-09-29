import webbrowser
import time
import os


 


print("Boardgame Time!")
game_choice= input("What game would you like to play? ")
if game_choice == "monopoly":
    print("going the money man route are ye?")
elif game_choice == "uno":    
    print("this isn't even a board game you scub")
elif game_choice == "scrabble":
    print("so many letters so little time")
    time.sleep(3)
    webbrowser.open('https://playoverwatch.com/en-us/heroes/sombra/')
elif game_choice == "anki":
    print("youre not even trying now")
    time.sleep(3)
    filepath = input()
    os.startfile(filepath)
        


