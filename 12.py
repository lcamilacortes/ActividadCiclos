#Escribir un programa que visualice la siguiente figura,
#utilizando ciclos. El usuario decide cuantas líneas quiere
#imprimir
a = int(input("Digite el primer número de filas: "))


for i in range (1, a+1):
    for j in range (i):
        print("*" ,end= "")
        
    print()