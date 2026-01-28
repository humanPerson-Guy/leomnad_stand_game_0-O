money=200
lemon=0
cup=0
ice=0
sugar=0

def add(num,num1):
    number= num+num1
    return number

buy=int(input("1 =lemon 2=cup 3=sugar 4=ice"))
buyness=int(input("how much you whant to buy"))
if buyness <= 0:
    print("please put in what you want to buy.")
elif buy==1:
    if mony<=buyness*-2+mony:
        print("you don't have enough.")
    else:
        mony=buyness*-2+money
        lemon=buyness
elif buy==2:
    if money<=buyness*-1+money:
        print("you don't have enough.")
    else:
        money=buyness*-1+money
        cupn=buyness
elif buy==3:
    if money<=buyness*-3+mony:
        print("your to poor")
    else:
        money=buyness*-3+money
        shuger=buyness
elif buy==4:
    if money<=buyness*-2+money:
        print("your to poor")
    else:
        money=buyness*-1+money
        ice=buyness
print (money)

