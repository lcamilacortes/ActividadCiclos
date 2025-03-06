#Solicitar al usuario un número de hasta 9 dígitos e
#imprimirlo en orden contrario. Ej. digito 6754 imprimo 4576

a = int(input("Digite un numero de maximo 9 cifras "))
inversa=0

while a>0:
    ultimo= a%10
    inversa= inversa *10+ultimo
    a=a//10

print("el valor a la inversa es ", inversa) 