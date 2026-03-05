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



hp=20


debt=1001
price=1
x=80
print("Now set your recipe for your lemonade. You can change this later.")

print("You should probably change your price from 1$.")
while day!=8 and die=="n":
    while die=="n":
        
        ch=input("What do you do. 1 for shop, 2 to see your goodies, 3 to set your lemonade price, 4 to change the recipe and anything else will emd the day.")
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
            if hp<=0:
                die="y"  
            if sanity<=4:
                print('The line of custimers faces are streched eyes ripped out skin peeling off but you need the money.')
            break
        if die=="y":
            break
        
       
    for i in range(1,random.randint(40,x)):
        c=Customer()
        tipe,buy=buyOrnobuy(c.get_customer_attributes(),recipe,price,lemonaids,recipe["cup"])
        
        if tipe.__contains__("eldrich entity"):
            sanity-=1
            if tipe=="eldrich entity dinosor":
                print("your mind goes numb")
            if tipe=="eldrich entity you":
                print("you see your self walk up to your lemonaid stand as it gets closer your vison gos blurry")
                print("a wave of pain floods your mind.")
                if buy=="y":
                    print("it doesn't matter though because they bought your lemonade.")
                        
        if tipe=="mafia":
                print("eh you got the goods. ")
                print("no well (takes out banana and points it at you).")
                if buy=="n":
                    hp-=1
                    print(".Your blood flows down the side walk none of the custimers seem to notice.")
                    if sanity<6:
                        sanity-=1  
                

        if buy=="y":
            goodies["money"]+=price
            lemonaids-=1
          
            goodies["cup"]-=recipe["cup"]
            goodies["lemon"]-=recipe["lemon"]
            goodies["sugar"]-=recipe["sugar"]
            goodies["ice"]-=recipe["ice"]
    
    day+=1
    trueday+=1
    sanity+=1
    if day==7 and money<debt:
        print("The boss looks at you face contorting flesh ripping apart. Your mind splits in two .Your flesh rips eyes roll back..... then it all stops.  ")
        print("You find your self in a infinite white void. Then it all ends")
        die="y"
 

        
    if trueday==4:
        hp+=1
    while die=="n":

        print("what would you like to do with your night. C, for crime. M, for meditation. G, for gambling. You can gamble as much as you want but the other two take time so you can only do them once.")
    
        cho=input()
        if cho=="g":
            w=random.choice(["n","n","n","n","y"])
            loses=input("how much are you gambling?")
            try:
                loses=float(loses)
            except ValueError:
                print("Your friend decides to bet for you because of your indecision.")
                loses=2
            else:
                if loses>money:
                    print("you're to poor")
                elif loses <0:
                    print("positive number idiot")    
                elif w=="n":
                    goodies['money']-=loses
                    print("you lost" + str(loses) + "dollars")
                    print(goodies['money'])
                elif w=="y":
                    goodies['money']+=loses
                    print("you won"+str(loses)+"dollars")
                    print(goodies['money'])
                
                    
        elif cho=="m":
            print("your mind reforms")
            sanity+=1
            break
        elif cho=="c":
            print("you comit a crime")   
            m=random.randint(-80,40)
            
            
                
            if m>0:
                print("you got"+str(m)+"money from your robery")
                goodies['money']+=m
            if m<0:
                print("You found lots of money but when you check your wallet. There's less money than what you started with.")
                print(m)
                goodies['money']+=m
            break
if die=="y":
    print('skill issue')
if die=="n":
    print('You win but did you really?')