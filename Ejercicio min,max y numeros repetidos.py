
"""
Solicitar al usuario 5 números,
imprimir el min y max, iindicar si entre dichos valor
hay numeros repetidos o no
"""


lista = []
cont = 0

while cont != 5:
    numeros = int(input("ingrese cinco numeros enteros: "))
    lista.append(numeros)
    cont = cont + 1

numeros = [lista]
if len(lista) == len(set(lista)):
    print("no hay repetidos")
else:
    print("hay numeros repetidos")
       
          
print(lista)    
print("numero menor: ",min(lista))
print("numero mayor: ",max(lista))


  
    
    