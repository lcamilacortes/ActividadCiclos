#Determinar cuales y cuantos números perfectos hay entre 1 y
#1000?

inicio=0
fin=100
cont= 0
suma=0
perfectos=""

num1= inicio
while num1 <= fin:
    suma= 0
    i = 1
    while i < num1:
        if num1 % i == 0:
            suma += i
        i += 1
    if suma == num1:
        perfectos += f"{num1} "
        cont += 1
    num1 += 1

print("numeros perfectos del 1 al 1000 son ", perfectos)

print("la cantidad de numeros perfectos es  ",cont)
