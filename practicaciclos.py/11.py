#Solicitar 2 números al usuario e imprimir el cociente y el
#residuo del mayor en el menor sin utilizar la división ni el mod. 


a = int(input("Digite el primer número: "))
b = int(input("Digite el segundo número: "))
cociente = 0
if a > b:
    mayor, menor = a, b
else:
    mayor, menor = b, a



residuo = mayor


while residuo >= menor:
    residuo -= menor
    cociente += 1

print("Cociente:", cociente)
print("Residuo:", residuo)
