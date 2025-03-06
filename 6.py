 #Calcular el máximo de números positivos introducidos por
#teclado, sabiendo que metemos números hasta que
#introduzcamos uno negativo. El negativo no cuenta. 
cont=0

while True:
 numax=int(input("digita un numero positivo para iniciar o un negativo para terminar"))

 if numax < 0:
  break

cont+=1
print(f"Has introducido {cont} números positivos.")