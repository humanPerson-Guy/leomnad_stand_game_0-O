from nigredants import shop


goodies=shop()
             

print(goodies["mony"])
print(goodies["lemon"])


chos=input("1=shop 2=change recipe 3=change price")


print(goodies)

respy={
    "lemon":1,
    "cup":1,
    "ice":1,
    "suger":1
}
#print(respy)

while True:
    print(respy['lemon'])
    respy['lemon']=int(input("how meny lemons per lemonad"))
    if respy['lemon']>=5:
        continue
    respy['cup']=int(input("how meny cups per lemonad"))
    if respy['cup']>=5:
        continue
    respy['ice']=int(input("how meny ice per lemonad"))
    if respy['cup']>=5:
        continue
    respy['suger']=int(input("how meny suger per lemonad"))
    if respy['suger']>=5:
        continue
    break

print(respy)
l=0
c=0
i=0
s=0
print(goodies)
nadCount={
    "lemon":goodies["lemon"],
    "cup":goodies["cup"],
    "ice":goodies["ice"],
    "suger":goodies["suger"]
}

while nadCount["lemon"] >0:
    nadCount['lemon']-=respy["lemon"]
    l+=1
if nadCount["lemon"] <0:
    nadCount['lemon']+=respy["lemon"]    
    l-=1

while nadCount["cup"] >0:
    nadCount['cup']-=respy["cup"]
    c+=1
if nadCount["cup"] <0:
    nadCount['cup']+=respy["cup"]    
    c-=1
while nadCount["ice"] >0:
    nadCount['ice']-=respy["ice"]
    i+=1
if nadCount["ice"] <0:
    nadCount['ice']+=respy["ice"]    
    i-=1
while nadCount["suger"] >0:
    nadCount['suger']-=respy["suger"]
    s+=1
if nadCount["suger"] <0:
    nadCount['suger']+=respy["suger"]    
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

    price=int(input("how expensive is your lemonad"))
    if price >100 or price<0:
        print("not valid price")
        continue
    else:
        break

print("price")
