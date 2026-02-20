from customer import Customer
import random
price=1
recipe={
    "lemon":1,
    "cup":1,
    "ice":1,
    "sugar":1
}
def buyOrnobuy(guy,recipe,price):
    
    
    goodness={
        "sweet":guy["sweetness"]-recipe['sugar'],
        "ice":guy["ice"]-recipe['ice'],

    }
   
    chance=["y","y","y"]
    while goodness["sweet"]!= 0:
        if goodness["sweet"]>0:
            chance.append("n")
            goodness["sweet"]-=1
        if goodness["sweet"]<0:
            chance.append("n")
            goodness["sweet"]+=1
       
    while goodness["ice"]!= 0:
        if goodness["ice"]>0:
            chance.append("n")
            goodness["ice"]-=1
        if goodness["ice"]<0:
            chance.append("n")
            goodness["ice"]+=1
     
     
    
    if guy["price"]+.50<price:
        chance.append("n")
        
    if guy["price"]+1<price:
       
        chance.append("n")
    if guy["price"]+1.5<price:
        chance.append("n")
        
    if guy["price"]+2.5<price:
        chance.append("n")
        chance.append("n")
        
    if guy["price"]+4<price:
        chance.append("n")
        chance.append("n")
        chance.append("n") 
        chance.append("n")
      
        chance.append("n")
    if guy["price"]+7.65<price:
        for r in range(1,10):
            chance.append("n")
        
    if guy["price"]+20<price:
        for i in range(1,20):
            chance.append("n")
    if guy["price"]+50<price:
        for i in range(1,100):
            chance.append("n")
    if guy["price"]+92<price:
        for i in range(1,800):
            chance.append("n")
   
    x=random.choice([" level 100 mafia boss"," borgison"," fesgiraf"," gilziblorp"," your mother"," bob"," you"," giraf"," dinosor"])
    print(random.choice(chance))
    custTipe=(random.choice(["guy","gal","guy","gal","mafia","mafia","gal","guy","eldrich entity"]))

    if custTipe=="eldrich entity":
        custTipe="eldrich entity"+x
    print(custTipe)

c=Customer()






