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
    chance=["y","y","y"]
    while goodness["sweet"]!= 0:
        if goodness["sweet"]>0:
            chance.append["n"]
            sweet+=1






c = Customer()

buyOrnobuy(c.get_customer_attributes(),recipe)

