print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."*` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.\nLegends tell of great treasure to be found here.")

print("After walking ashore, the path splits.")

choice1 = input("Which way will you go? Type 'left' or 'right':\n").lower()
if choice1 == "left":
    print("You come to a lovely lake with an island in the middle.")

    choice2 = input("Enter 'wait' to wait for a boat, or enter 'swim' to swim to the island:\n").lower()
    if choice2 == "wait":
        print("Eventually, a boatman draws near and offers you a ride to the island.")
        print("There you find a stately-looking house with three colored doors.")

        choice3 = input("Which door will you choose? Enter 'red,' 'yellow,' or 'blue':\n").lower()
        if choice3 == "red":
            print("Oh my, it's a bit warm in here. Warm and bright.")
            print("That's because you've fallen into a blazing furnace.")

        elif choice3 == "blue":
            print("This room is dark.")

            choice4 = input("Will you light a match? Enter 'y' for yes or 'n' for no:\n").lower()
            if choice4 == "y":
                print("The small flame is reflected by a dozen large green eyes.")
            else:
                print("That's probably for the best.")
            print("You are in a den of gigantic kittens, and you are their new toy.")
            print("RIP.")

        elif choice3 == "yellow":
            print("Your eyes are dazzled by mountains of gold. You found the treasure! Huzzah!")
            print("I'll give you a moment to celebrate before I mention the tax bracket for such obscene wealth.")
            print("Enjoy!")

    else:
        print("You had nearly reached the island when you encountered a school of ravenous piranhas.")
        print("Bon appetit for them, I suppose.")

else:
    print("Oh dear, a rogue boulder smashes through the trees and comes to a rest right on top of you.")
    print("What a brief, pitiful story this has been.")

print("\n")
print("The End")
