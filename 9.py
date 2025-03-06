#Calcular la operación x n
 #sin utilizar la función pow
x=int(input("digita el valor x"))
n=int(input("digita la potencia de n"))
cont=0
resultado=1
print(f"{x} elevado a {n} es: ")
while cont < n:
    resultado=resultado*x
    cont +=1
    
print(f"{resultado}")
    
