from recipe import resipyChanger,pricer
from customer import Customer
from introduction import intro
from ingredients import shop
from nobuy import buyOrnobuy
recipe={
    "lemon":1,
    "cup":1,
    "ice":1,
    "sugar":1
}
money, name,hardness=intro()
print(hardness)
goodies=shop(money)
ch=input("what do you do 1 shop 2 see yoour goodies 3 set your lemonad price 4 change the recipe")
if ch== "1":
    goodies=shop(money)
if ch== "2":
    print (goodies)
if ch== "3":
   price=pricer()
if ch== "4":
    recipe=resipyChanger()