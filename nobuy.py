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
        "sweet":guy["sweet"]-recipe["sugar"],
        "lemon":guy["lemon"]-recipe["lemon"],
        "ice":guy["ice"]-recipe["ice"],
    }
    print(goodness)

buyOrnobuy(1,recipe)

