from custmer import custmer
import random

resipy={
    "lemon":1,
    "cup":1,
    "ice":1,
    "suger":1
}
def buyOrnobuy(guy,recipy):
    goodness={
        "sweet":guy["sweet"]-recipy["suger"],
        "lemon":guy["lemon"]-recipy["lemon"],
        "ice":guy["ice"]-recipy["ice"],
    }
    print(goodness)
buyOrnobuy(1,resipy)