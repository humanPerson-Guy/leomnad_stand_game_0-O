def add(num,num1):
        number= num+num1
        return number

def shop(money=100,lemon=10,cup=10,ice=10,sugar=10):

    buy=int(input("1 =lemon 2=cup 3=sugar 4=ice"))
    buyness=int(input("how much do you whant to buy?"))
    if buyness <= 0:
        print("go back")
    elif buy==1:
        if money<=buyness*-2+money:
            print("you dont have enough.")
        else:
            money=buyness*-2+money
            lemon=buyness
    elif buy==2:
        if money<=buyness*-1+money:
            print("you dont have enough.")
        else:
            money=buyness*-1+money
            cup=buyness
    elif buy==3:
        if money<=buyness*-3+money:
            print("you don't have enough.")
        else:
            money=buyness*-3+money
            sugar=buyness
    elif buy==4:
        if money<=buyness*-2+money:
            print("your to poor")
        else:
            money=buyness*-1+money
            ice=buyness
    print (lemon,cup,ice,sugar,money)
    return lemon,cup,ice,sugar,money

shop(600,0,0,0,0)