def add(num,num1):
        number= num+num1
        return number

def shop(mony=100,lemon=10,cup=10,ice=10,shuger=10):

    buy=int(input("1 =lemon 2=cup 3=shuger 4=ice"))
    buyness=int(input("how much you whant to buy"))
    if buyness <= 0:
        print("you diry")
    elif buy==1:
        if mony<=buyness*-2+mony:
            print("your to poor")
        else:
            mony=buyness*-2+mony
            lemon=buyness
    elif buy==2:
        if mony<=buyness*-1+mony:
            print("your to poor")
        else:
            mony=buyness*-1+mony
            cup=buyness
    elif buy==3:
        if mony<=buyness*-3+mony:
            print("your to poor")
        else:
            mony=buyness*-3+mony
            shuger=buyness
    elif buy==4:
        if mony<=buyness*-2+mony:
            print("your to poor")
        else:
            mony=buyness*-1+mony
            ice=buyness
    print (lemon,cup,ice,shuger,mony)
    return lemon,cup,ice,shuger,mony
shop(600,0,0,0,0)