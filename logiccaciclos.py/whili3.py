#Secuencia de Collatz: Crea un programa que genere la secuencia de Collatz (también conocida como la conjetura de 3n+1) para un número n introducido por el usuario hasta llegar a 1

#La secuencia de Collatz es una sucesión de números que se genera a partir de un entero positivo, siguiendo ciertas reglas. La conjetura de Collatz afirma que, sin importar el número inicial, la secuencia siempre termina en 1. 
#  Cómo se construye la secuencia
#Se toma un número entero positivo 
#Si el número es par, se divide entre 2 
#Si el número es impar, se multiplica por 3 y se le suma 1 
#e repite el proceso con cada número que surge de las operaciones 
n=int(input("digite un numero entero positivo: "))
if n<=0:
    print("numero no valido")  
else:
    while n!=1:
        if n%2==0:
            n=n/2
            print(n)
        else:
            n=n*3+1
            print(n)    
          