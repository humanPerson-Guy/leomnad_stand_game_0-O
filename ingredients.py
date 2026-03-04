

def add(num,num1):
        number= num+num1
        return number
#this sets the basis for the code
def shop(goodies):
#player starting stats
    money=goodies["money"]
    cup=goodies["cup"]
    lemon=goodies["lemon"] #stuff
    sugar=goodies["sugar"]
    ice=goodies["ice"]
    while True:
        buy=(input("1 =lemon 2=cup 3=sugar 4=ice "))
        try:
            buy=int(buy)
        except ValueError:
            print("i need a number idiot")
        else:
            break
    while True:
        buyness =(input ("How much would you like to buy? "))

        try:
            buyness=int(buyness)
        except ValueError:
            print("i need a number idiot")
        else:
            break
    
    if buyness <= 0:
        print("you didn't buy anything.")
    elif buy==1:
        if money<=buyness*-0.5123+money:
            print("you don't have enough")
        else:
            money=buyness*-0.5123+money
            lemon+=buyness
    elif buy==2:
        if money<=buyness*-0.4654647+money:
            print("you made a purchase")
        else:
            money=buyness*-0.4654647+money
            cup+=buyness
    elif buy==3:
        if money<=buyness*-0.467+money:
            print("you don't have enough")
        else:
            money=buyness*-0.467+money
            sugar+=buyness
    elif buy==4:
        if money<=buyness*-0.303+money:
            print("you dont have enough")
        else:
            money=buyness*-0.303+money
            ice+=buyness
    
    goodies={
        "lemon":lemon,
        "cup":cup,
        "ice":ice,
        "sugar":sugar,
        "money":money
    }
    print(goodies)
    
      
    return goodies
#shop(600,0,0,0,0)

#this completes the purchase

