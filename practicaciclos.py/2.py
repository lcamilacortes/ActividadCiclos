# Determinar si un numero es o no es primo

num=int (input("digite un valor "))
cont=0
for i in range(1,num+1):
    if num%i==0:
        cont+=1
if cont==2:
    print(f"{num} es primo")
else:
    print(f"{num} no es primo")
    