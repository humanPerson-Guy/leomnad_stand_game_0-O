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
goodies={
    
}
money, name=intro()
if money==0.2:
    x=1
    debt=10002
else :
    debt=1001
while True:
    goodies=shop(money)
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
        break
for i in range(1,random.randint(x,3)):
    c=Customer()