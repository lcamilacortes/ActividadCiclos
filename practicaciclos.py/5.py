inicio =0
fin=1000
cont= 0
primo=""

num1= inicio
while num1 <= fin:
    a1 = 0
    i = 1
    while i < num1:
        if num1 % i == 0:
            a1 += i
        i += 1
    if a1 == 1:
        primo += f"{num1} "
        cont += 1
    num1 += 1

print("numeros primos del 1 al 1000 son ", primo)
print("la cantidad de numeros primos es  ",cont)



