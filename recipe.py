from ingredients import shop
<<<<<<< HEAD


goodies = shop()
=======

#imports shop function
goodies=shop()
             
>>>>>>> bd34c6364d78a7a562e914fd82147ba58e50218f

print(goodies["money"])
print(goodies["lemon"])

<<<<<<< HEAD

choose=input("1 = shop, 2 = change recipe, 3 = change price ")
=======
#sets up first ingridients
choose=input("1=shop 2=change recipe 3=change price")
>>>>>>> bd34c6364d78a7a562e914fd82147ba58e50218f


print(goodies)

recipe={
   "lemon":1,
    "cup":1,
    "ice":1,
    "sugar":1
}
#print(recipe)

while True:
    print(recipe['lemon'])
    recipe['lemon']=int(input("how many lemons per cup?"))
    if recipe['lemon']>=5:
        continue
    recipe['cup']=int(input("how many cups per lemonad"))
    if recipe['cup']>=5:
        continue
    recipe['ice']=int(input("how much ice per cup?"))
    if recipe['cup']>=5:
        continue
    recipe['sugar']=int(input("how much sugar per cup?"))
    if recipe['sugar']>=5:
        continue
    break

print(recipe)
l=0
c=0
i=0
s=0
print(goodies)
nadCount={
    "lemon":goodies["lemon"],
    "cup":goodies["cup"],
    "ice":goodies["ice"],
    "sugar":goodies["sugar"]
}

while nadCount["lemon"] >0:
    nadCount['lemon']-=recipe["lemon"]
    l+=1
if nadCount["lemon"] <0:
    nadCount['lemon']+=recipe["lemon"]    
    l-=1

while nadCount["cup"] >0:
    nadCount['cup']-=recipe["cup"]
    c+=1
if nadCount["cup"] <0:
    nadCount['cup']+=recipe["cup"]    
    c-=1
while nadCount["ice"] >0:
    nadCount['ice']-=recipe["ice"]
    i+=1
if nadCount["ice"] <0:
    nadCount['ice']+=recipe["ice"]    
    i-=1
while nadCount["sugar"] >0:
    nadCount['sugar']-=recipe["sugar"]
    s+=1
if nadCount["sugar"] <0:
    nadCount['sugar']+=recipe["sugar"]    
    s-=1
print(nadCount)
print(l,c,i,s)
todnads=0
while True:
    if not(l<=0)and not(c<=0) and not(i<=0) and not(s<=0):
        print("yugblkrfgetdhbjv")
        todnads+=1
        l-=1
        c-=1
        i-=1
        s-=1
    else:
        break   
print(todnads)






while True:

    price=int(input("how expensive is your lemonade?"))
    if price >100 or price<0:
        print("not a valid price")
        continue
    else:
        break

print("price")
