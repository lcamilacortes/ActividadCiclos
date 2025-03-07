#((Una progresión aritmética es una sucesión de números en la que cada término se obtiene sumando una misma cantidad al término anterior. A esta cantidad se le llama diferencia común. 
#Ejemplos 
#3, 5, 7, 9, ... es una progresión aritmética con diferencia constante 2.
#5, 2, −1, −4, ... es una progresión aritmética con diferencia constante −3))

inicio=int(input("digite el valor de inicio: "))
diferencia=int(input("digite los saltos de la progresion matematica: "))
fin=int(input("digite hasta que numero desea llegar: "))

for i in range(inicio,fin,diferencia):
    print(i)