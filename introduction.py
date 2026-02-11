# This code will be introduction of the game
money = 0

name = input("Enter your name: ")
print("Hello", name ,"welcome to lemonade stand! In this game you will sell lemonade to customers. The goal is to get the most days possible. The rules are very simple you start off with a amount of money and buy ingredients and create a recipe for your customers. If you end up with no money you go bankrupt and loose.")
#this welcomes the user and tells them the main objective.
while True:
    difficulty = input("Choose difficulty Easy/Medium/Hard/Impossible: ")
    if difficulty == "Easy":
        money = 600
        print("You have 600 dollars.")
        break
#this puts them at the easiest difficulty, starting them with $600
    elif difficulty == "Medium":
        money = 400
        print("You have 400 dollars.")
        break
#this puts them at the 2nd easiest difficulty, starting them with $400
    elif difficulty == "Hard":
        money = 200
        print("You have 200 dollars.")
        break
#this puts them at the 2nd hardest difficulty, starting them with $200
    elif difficulty == "Impossible":
        money = 100
        print("You have 100 dollars")
        break
#this puts them at the hardest difficulty, starting them with $100
    else:

        print("This input is not valid.")

#this code sets up their level and the amount of money they start out with.
