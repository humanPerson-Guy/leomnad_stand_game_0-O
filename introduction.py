# This code will be introduction of the game


def intro():
    print("Last week you needed to take a loan; your credit score was...low so you had to look for alternitive loaners.You had the bright idea to turn to the Lake Shore Mafia. You needed 600 dollars to buy your cat medicine. You forgot about your loan and /n" \
    "after 4 minutes it rose from $600 to $1000; So you made a lemonade stand to pay off your debt. The mafia is hunting you, Bribe them with good lemonade to give you more time to pay off your loan. If by the end of 7 days you cant pay off your debt you may not be a very happy camper."
    )
    name = input("Enter your name: ")
    print("Hello", name ,","welcome to lemonade stand! In this game you will sell lemonade to customers. The goal is to not die from the mafia. The rules are very simple",name,"start off with a amount of money and buy ingredients and create a recipe for your customers. If you end up with no money you go bankrupt and the mafia gets you at the end of 7 days. you need 1000$ to pay of your debt. good luck!")

    
<<<<<<< HEAD
    difficulty = input("Choose difficulty Easy/Medium/Hard/Impossible: ")
    if difficulty == "Easy" or "1":
        print("You have 600 dollars.")
        money = 600
    elif difficulty == "Medium" or "2":
        print("You have 400 dollars.")
        money = 400    
    elif difficulty == "Hard" or "3":
        print("You have 200 dollars.")
        money = 200    
    elif difficulty == "Impossible" or "4":
        print("You have 100 dollars")
        money = 99.68    
    elif difficulty == "ez":
        print("you have nothing")
        money=0.2
        
    else:
        print("dumy ")
        mony=-99999999999998
    return money,name
=======
difficulty = input("Choose difficulty Easy/Medium/Hard/Impossible: ")
    while True:
        if difficulty == "Easy" or "1":
            print("You have 600 dollars.")
            money = 600
        elif difficulty == "Medium" or "2":
            print("You have 400 dollars.")
            money = 400    
        elif difficulty == "Hard" or "3":
            print("You have 200 dollars.")
            mony = 200    
        elif difficulty == "Impossible" or "4":
            print("You have 100 dollars")
            money = 99.68    
        elif difficulty == "ez":
            print("you have nothing")
            mony=0.2
        else:
             print("invalid input")
            return money,name
>>>>>>> 0407fca2208e98c5cd7430ba062bf87d2ea47a65







