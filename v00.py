import os
import random 

potencia = random.seed(42)
numero = random.seed(42)
digt4 = (potencia**numero)

digt1 = (numero % 9)
digt2 = (potencia % 9)
digt3 = (numero % 9)
digt4 = (digt4 % 9)


print(digt1 + ' ' + digt2 + ' ' + digt3 + ' ' + digt4)