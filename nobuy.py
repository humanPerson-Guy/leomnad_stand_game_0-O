from customer import Customer
import random

recipe={
    "lemon":1,
    "cup":1,
    "ice":1,
    "sugar":1
}
def buyOrnobuy(guy,recipe):
    
    
    goodness={
        "sweet":guy["sweetness"]-recipe["sugar"],
        "ice":guy["ice"]-recipe["ice"],

    }
    print(guy)
    chance=["y","y","y"]
    while goodness["sweet"]!= 0:
        if goodness["sweet"]>0:
            chance.append("n")
            goodness["sweet"]-=1
        if goodness["sweet"]<0:
            chance.append("n")
            goodness["sweet"]+=1
        print(goodness["sweet"])
    while goodness["ice"]!= 0:
        if goodness["ice"]>0:
            chance.append("n")
            goodness["ice"]-=1
        if goodness["ice"]<0:
            chance.append("n")
            goodness["ice"]+=1
        print(goodness["ice"])
    print(chance)    
    
        
       




c = Customer()

buyOrnobuy(c.get_customer_attributes(),recipe)

