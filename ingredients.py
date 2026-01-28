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
        cupn=buyness
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
print (mony)
