n=int(input("digite un numero de 2 o mas digitos positivos"))
  
suma = 0  

while n != 0:  
    suma += n % 10  
    n //= 10   

print(f"La suma de los dígitos es: {suma}")  
