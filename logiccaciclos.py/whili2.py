#Adivina el número: Escribe un programa que permita al usuario adivinar un número entre 1,# generando un número aleatorio. El ciclo debe continuar pidiendo al usuario adivinaciones hasta que adivine correctamente
import random
n=random.randint(1,100)
print(n)

intento=0
while intento!=n:
    intento=int(input("adivina el numero: "))
    
print("el valor que digitaste es el correcto")
