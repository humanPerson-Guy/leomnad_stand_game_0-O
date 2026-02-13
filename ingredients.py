from introduction import money_two
#this completes the purchase
def add(num,num1):
        number= num+num1
        return number
#this sets the basis for the code
def shop(money=money_two,lemon=10,cup=10,ice=10,sugar=10):
#player starting stats
    buy=int(input("1 =lemon 2=cup 3=sugar 4=ice "))
    buyness = ("How much would you like to buy? ")
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
            cup=+buyness
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
    print (lemon,cup,ice,sugar,money)
    goodies={
        "lemon":lemon,
        "cup":cup,
        "ice":ice,
        "sugar":sugar,
        "money":money
    }
    return goodies
#shop(600,0,0,0,0)

#this completes the purchase
