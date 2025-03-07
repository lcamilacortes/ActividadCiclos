#->Serie de números Fibonacci de largo arbitrario: Escribe un programa que imprima los primeros n números de la secuencia Fibonacci, donde n es ingresado por el usuario

n=int(input("digite el valor de la serie "))

a,b=0,1
for i in range (0,n):
    if n==1:
        print("0")
        break
    if n==2:
        print("1")
        break
    print(a)
    a,b= b,a+b
    
    



