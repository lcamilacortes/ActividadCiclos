#Encontrar un número natural n más pequeño tal que la suma
#de los n primeros números naturales (1 + 2 + 3 + 4…..)
#exceda de una cantidad (máximo) introducida por el teclado.
#Es decir cuantos números de la serie de los naturales debo
#sumar para superar el dato máximo.

numax=int(input("digita el dato max"))
cont=0
acumulacion=0

while acumulacion <= numax:
    cont +=1
    acumulacion += cont

print(f"el numero natural mas pequeño que supera al {numax} es {cont}.")
print(f"la suma de los primeros {cont} numeros naturales es :{acumulacion}.")
