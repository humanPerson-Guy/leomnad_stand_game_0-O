

def add(num,num1):
        number= num+num1
        return number
#this sets the basis for the code
def shop(goodies):
#player starting stats
    money=goodies["money"]
    cup=goodies["cup"]
    lemon=goodies["lemon"]
    sugar=goodies["sugar"]
    ice=goodies["ice"]
    buy=int(input("1 =lemon 2=cup 3=sugar 4=ice "))
    buyness =int(input ("How much would you like to buy? "))
    if buyness <= 0:
        print("you didn't buy anything.")
    elif buy==1:
        if money<=buyness*-2+money:
            print("you don't have enough")
        else:
            money=buyness*-2+money
            lemon+=buyness
    elif buy==2:
        if money<=buyness*-1+money:
            print("you made a purchase ")
        else:
            money=buyness*-1+money
            cup+=buyness
    elif buy==3:
        if money<=buyness*-3+money:
            print("you don't have enough")
        else:
            money=buyness*-3+money
            sugar+=buyness
    elif buy==4:
        if money<=buyness*-2+money:
            print("you dont have enough")
        else:
            money=buyness*-1+money
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
