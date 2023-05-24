# ejemplo de uso de repositorio

from operator import truediv
from pickle import TRUE


print("datos personales")
print("-----------------------")
vNom = input("ingrese su nombre : ")
while True:
    try:
        vEdad = int(input("ingrese su edad : "))
        break
    except:
        print("valor no correspondiente")
print("-------------------------------")
print(f"su nombre es : {vNom}")
print(f"su edad es : {vEdad}")