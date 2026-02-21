from recipe import resipyChanger,pricer
from customer import Customer
from introduction import intro
from ingredients import shop
from nobuy import buyOrnobuy
import random
recipe={
    "lemon":1,
    "cup":1,
    "ice":1,
    "sugar":1
}
die="n"
money, name=intro()
goodies={
    "money":money,
    "cup":0,
    "lemon":0,
    "sugar":0,
    "ice":0
}
print("you need to buy suplys")

goodies=shop(goodies)
print("you need to set your resipy ")
lemonaids, recipe=resipyChanger(goodies)
if money==0.2:
    x=1
    debt=10002
else :
    debt=1001
price=1
x=3
print("you should probly change your price from 1$")
while die=="n":
    
    ch=input("what do you do 1 shop 2 see yoour goodies 3 set your lemonad price 4 change the recipe and any thing else to end day")
    if ch== "1":
        goodies=shop(goodies)
    elif ch== "2":
        print (goodies)
    elif ch== "3":
        price=pricer()
    elif ch== "4":
        recipe=resipyChanger(goodies)
    else:
        print("custimers are aproching")
        if goodies["money"]<=0:
            die="y"
        break
for i in range(1,random.randint(1,x)):
    c=Customer()
    tipe,buy=buyOrnobuy(c.get_customer_attributes(),recipe,price,lemonaids)
    if buy=="y":
        goodies["money"]+=price
        print(goodies["money"])
    