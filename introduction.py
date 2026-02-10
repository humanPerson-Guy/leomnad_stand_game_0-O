# This code will be introduction of the game
money = 0

name = input("Enter your name: ")
print("Hello", name ,"welcome to lemonade stand! In this game you will sell lemonade to customers. The goal is to get the most days possible. The rules are very simple you start off with a amount of money and buy ingredients and create a recipe for your customers. If you end up with no money you go bankrupt and loose.")
def intro():
    while True:
        difficulty = input("Choose difficulty Easy/Medium/Hard/Impossible: ")
        if difficulty == "Easy":
            print("You have 600 dollars.")
            return
        elif difficulty == "Medium":
            print("You have 400 dollars.")
            return
        elif difficulty == "Hard":
            print("You have 200 dollars.")
            return
        elif difficulty == "Impossible":
            print("You have 100 dollars")
            return
        else:

            print("This input is not valid.")

money = intro()