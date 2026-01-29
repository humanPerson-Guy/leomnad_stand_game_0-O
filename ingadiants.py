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
    print("please try again.")
elif buy==1:
    money=buyness*-2+money
    lemon=buyness
elif buy==2:
    money=buyness*-1+money
    cup=buyness
elif buy==3:
    money=buyness*-3+money
    sugar=buyness
elif buy==4:
    money=buyness*-20+money
    ice=buyness

print (money)
