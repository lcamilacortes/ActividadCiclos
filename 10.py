#Algoritmo para hallar el m.c.d de dos números m y n por
#el algoritmo de Euclides. 

m= int(input("digite el primer numero"))
n= int(input("digite segundo numero"))

while n != 0:
    r= m%n
    m = n
    n = r

print("el MCD es", m)