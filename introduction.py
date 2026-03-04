# This code will be introduction of the game


def intro():
    print("5 minutes ago you took a loan. Your credit score was... low so you had to look for alternitive loaners. You decided to turn to the Mafia. You needed $600 to buy your cat medicine. You forgot about your loan and" \
    "after 4 minutes it raised from $600 to $1001. So you made a lemonade stand as one of your part time jobs. The mafia is hunting you, bribe them with good lemonade to let you live longer. If by the end of 7 days you cant pay off your debt you won't be a very happy camper!"
    )
    name = input("Enter your name: ")
    print("Hello", name ,"welcome to lemonade stand! In this game you will sell lemonade to customers. The goal is to not die from the mafia. The rules are very simple",name,"start off with a amount of money and buy ingredients and create a recipe for your customers. If you end up with no money you go bankrupt and the mafia gets you at the end of 7 days you need 1000$ to pay of your debt to the mafia good luck.")

    

    
    while True:
        difficulty = input("Choose difficulty Easy/Medium/Hard/Impossible/Ez: ")
        if difficulty.lower() == "easy" or difficulty == "1":
            print("You have 600 dollars.")
            money = 600
        elif difficulty.lower() == "medium" or difficulty == "2":
            print("You have 400 dollars.")
            money = 400
        elif difficulty.lower() == "hard" or difficulty == "3":
            print("You have 200 dollars.")
            money = 200
        elif difficulty.lower() == "impossible" or difficulty == "4":
            print("You have 100 dollars")
            money = 99.68
        elif difficulty.lower() == "ez":
            print("you have nothing")
            money = 0.2
        else:
            print("invalid input")
            continue

        return money,name