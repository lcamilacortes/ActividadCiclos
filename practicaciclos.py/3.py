# Determinar si un número es o no es perfecto. Un numero es
#perfecto si la suma de sus divisores sin incluir el propio
#número es igual a este 

num1 = int(input("Ingresa un número: "))

suma = 0
i = 1  
while i < num1:  
    if num1 % i == 0: 
        suma += i
    i += 1


if suma == num1:
    print(f"{num1} es un número perfecto.")
else:
    print(f"{num1} no es un número perfecto.")
