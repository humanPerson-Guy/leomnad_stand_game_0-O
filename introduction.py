# This code will be introduction of the game


def intro():
    name = input("Enter your name: ")
    print("Hello", name ,"welcome to lemonade stand! In this game you will sell lemonade to customers. The goal is to not die from the mafia. The rules are very simple ",name," start off with a amount of money and buy ingredients and create a recipe for your customers. If you end up with no money you go bankrupt and the mafia gets you at the end of 7 days you need 1000$ to pay of your debt to the mafia good luck.")

    
    difficulty = input("Choose difficulty Easy/Medium/Hard/Impossible: ")
    if difficulty == "Easy" or "1":
        print("You have 600 dollars.")
        mony=600
    elif difficulty == "Medium" or "2":
        print("You have 400 dollars.")
        mony=400
        hardness="good boy"
    elif difficulty == "Hard" or "3":
        print("You have 200 dollars.")
        mony=200
        hardness="good boy"
    elif difficulty == "Impossible" or "4":
        print("You have 100 dollars")
        mony=99.68
        hardness="good boy"
    else:
        print("you have choisen death")
        hardness="DETH"
        return mony,name,hardness




