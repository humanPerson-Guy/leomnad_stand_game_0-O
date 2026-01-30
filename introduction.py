# This code will be introduction of the game
money = 0

name = input("Enter your name: ")
print("Hello", name ,"welcome to lemonade stand! In this game you will sell lemonade to customers. The goal is to get the most days possible. The rules are very simple you start off with a amount of money and buy ingredients and create a recipe for your customers. If you end up with no money you go bankrupt and loose.")

while True:
    difficulty = input("Choose difficulty Easy/Medium/Hard/Impossible: ")
    if difficulty == "Easy":
        money = 600
        print("You have 600 dollars.")
    elif difficulty == "Medium":
        money = 400
        print("You have 400 dollars.")
    elif difficulty == "Hard":
        money = 200
        print("You have 200 dollars.")
    elif difficulty == "Impossible":
        money = 100
        print("You have 100 dollars")
        break
    else:
        print("This input is not valid.")