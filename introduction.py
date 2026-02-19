# This code will be introduction of the game


def intro():
    name = input("Enter your name: ")
    print("5 minets ago you took a lone your credet score was -12 so you had to look for alturnidive loners. so you turned /n to the Mafia.You needed 6 dolars to buy your cat medicin.You forgot about you lone and /n" \
    "after 4 minets it rose from 6$ to 1001$.So  you made a lemonaid stand .the mafia is hunting you bribe them with good lemanaid to let you live longer.if by the end of 7 days you cant pay off your debt you becom a rat /n" \
    )
    print("Hello", name ,"welcome to lemonade stand! In this game you will sell lemonade to customers. The goal is to not die from the mafia. The rules are very simple ",name," start off with a amount of money and buy ingredients and create a recipe for your customers. If you end up with no money you go bankrupt and the mafia gets you at the end of 7 days you need 1000$ to pay of your debt to the mafia good luck.")

    
    difficulty = input("Choose difficulty Easy/Medium/Hard/Impossible: ")
    if difficulty == "Easy" or "1":
        print("You have 600 dollars.")
        mony=600
    if difficulty == "Medium" or "2":
        print("You have 400 dollars.")
        mony=400    
    if difficulty == "Hard" or "3":
        print("You have 200 dollars.")
        mony=200    
    if difficulty == "Impossible" or "4":
        print("You have 100 dollars")
        mony=99.68    
    if difficulty == "ez":
        print("you have nothing")
        mony=0.2
    else:
        print("you have choisen death")
        mony=7.5   
    return mony,name




