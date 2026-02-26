from recipe import resipyChanger,pricer,lemonais_count
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
    "cup":2,
    "lemon":2,
    "sugar":2,
    "ice":2
}
day=1
timeguy=1
trueday=1

sanity=10-random.randint(1,3)



hp=7
if money==0.2:
    x=1
    hp=2
    sanity=6-random.randint(1,2)
    debt=10002
else :
    debt=1001
price=1
x=5
print("now set your resipe for your lemondid . you can change this later")

print("you should probly change your price from 1$")
while day!=8 and die=="n":
    while True:
        
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
            lemonaids=lemonais_count(goodies)
            if goodies["money"]<=0:
                die="y"
                
            break
        lemonaids=lemonais_count(goodies)
       
    for i in range(1,random.randint(x,8)):
        c=Customer()
        tipe,buy=buyOrnobuy(c.get_customer_attributes(),recipe,price,lemonaids,recipe["cup"])
        
        if tipe.__contains__("eldrich entity"):
            sanity-=1
            if tipe=="eldrich entity dinosor":
                print("your mind gos numb")
            if tipe=="eldrich entity you":
                print("you see your self walk up to your lemonaid stand as it gets closer your vison gos blurry")
                print("a wave of pain floods your mind .")
                if buy=="y":
                    print("it dusint matter tho cuz thay bought your lemonaid")
    
        if day==7 and timeguy==1:
            timeguy+=1
        if tipe=="mafia":
                print("eah you got the goods ")
                print("no well (takes out banana and points it at you).")
                if buy=="n":
                    hp-=1
                    print(".Your blood flows down the side walk none of the custimers seem to notice.")
                    if sanity<6:
                        sanity-=1  
                

        if buy=="y":
            goodies["money"]+=price
            lemonaids-=1
            print(goodies["money"])
            goodies["cup"]-=recipe["cup"]
            goodies["lemon"]-=recipe["lemon"]
            goodies["sugar"]-=recipe["sugar"]
            goodies["ice"]-=recipe["ice"]

    day+=1
    trueday+=1
    sanity+=1
    if day==4:
        hp+=1
    
        