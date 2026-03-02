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
            if hp<=0:
                die="y"  
            if sanity<=4:
                print('the line of custimers faces are streched eyes ripped out skin pealing off but you need the money')
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
    if day==7 and money<debt:
        print("the boss looks at you face contorting flesh ripping apart . your mind splits in two .Your flesh rips eyes roll back..... then it all stops  ")
        print("you find your self in a infinet white void . then it all")
        print("         ,----.  .-._                      ,-,--. " )
        print(',-.--` , \/==/ \  .-._  _,..---._  ,-.-  _')
        print( '|==|-  _.-`|==|, \/ /, /==/,   -  \/==/_ ,_.')
        print( '  |==|   `.-.|==|-  \|  ||==|   _   _\==\  \ ' ) 
        print('/==/_ ,    /|==| ,  | -||==|  .=.   |\==\ -\  ') 
        print('|==|    .- |==| -   _ ||==|,|   | -|_\==\ ,\'' )
        print('|==|_  ,`-._|==|  /\ , ||==|     /==/\/ _ |')
        print('/==/ ,     //==/, | |- ||==|-,   _`/\==\ - , / ')
        print('`--`-----`` `--`./  `--``-.`.____.  `--`---   ')

        
    if trueday==4:
        hp+=1
    while True:

        print("what whould you like to do with your night .1 for crime .2 for meditation.3 for gambling.")
    
        cho=input()
        if cho==4:
            w=random.choice(["n","n","n","y"])
            loses=input("how much you gmbling")
            try:
                loses=float(loses)
            except ValueError:
                print("your firend disides to bet for you becose of your indicition.")
                loses=2
            if w=="n":
                money-=loses
                print("you lost"+str(loses)+"dolors")
            if w=="y":
                money+=loses
                print("you won"+str(loses)+"dolors")
                
        elif cho==2:
            print("your mind reforms")
            sanity+=1
        elif cho==1:
            print("you comit a crime")   
            m=random.randint(-1,-3.48,-2,-3,-56,-2.3,-1.3,-4.93,1,-2,1,1,1,-1,-1,-2,4.4,3.57,-2.34,1.34,1.563,1,2,3,34,12,6.7)
            print("you got "+str(m)+" money")
            print()

