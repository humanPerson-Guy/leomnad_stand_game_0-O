mony=200
lemon=0
cup=0
ice=0
shuger=0

def add(num,num1):
    number= num+num1
    return number

buy=int(input("1 =lemon 2=cup 3=shuger 4=ice"))
buyness=int(input("how much you whant to buy"))
if buyness <= 0:
    print("you diry")
elif buy==1:
    mony=buyness*-2+mony
    lemon=buyness
elif buy==2:
    mony=buyness*-1+mony
    cup=buyness
elif buy==3:
    mony=buyness*-3+mony
    shuger=buyness
elif buy==4:
    mony=buyness*-20+mony
    ice=buyness
print (mony)