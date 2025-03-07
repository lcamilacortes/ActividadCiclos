#Determinar cuales son los múltiplos de 5 comprendidos entre
#1 y N

N = int(input("Ingresa el valor de N: "))
i=0
print(f"los multiplos de 5 comprendidos entre 1 y {N} son:" )
for i in range (i,N+1,5):
    if i % 5 == 0:
      print(f"{i}")  
      
      

  