# This code will be introduction of the game


def intro():
    print("5 minutes ago you took a loan your credit score was -12 so you had to look for alternitive loaners. so you turned in to the Mafia. You needed 6 dollars to buy your cat medicine. You forgot about your loan and /n" \
    "after 4 minutes it rose from 6$ to 1001$. So you made a lemonade stand as one of your part time jobs. The mafia is hunting you bribe them with good lemonade to let you live longer. If by the end of 7 days you cant pay off your debt you becom a rat"
    )
    name = input("Enter your name: ")
    print("Hello", name ,"welcome to lemonade stand! In this game you will sell lemonade to customers. The goal is to not die from the mafia. The rules are very simple",name,"start off with a amount of money and buy ingredients and create a recipe for your customers. If you end up with no money you go bankrupt and the mafia gets you at the end of 7 days you need 1000$ to pay of your debt to the mafia good luck.")

    
difficulty = input("Choose difficulty Easy/Medium/Hard/Impossible: ")
    while True:
        if difficulty == "Easy" or "1":
            print("You have 600 dollars.")
            mony = 600
        elif difficulty == "Medium" or "2":
            print("You have 400 dollars.")
            mony = 400    
        elif difficulty == "Hard" or "3":
            print("You have 200 dollars.")
            mony = 200    
        elif difficulty == "Impossible" or "4":
            print("You have 100 dollars")
            mony = 99.68    
        elif difficulty == "ez":
            print("you have nothing")
            mony=0.2
        else:
             print("invalid input")
            return mony,name



