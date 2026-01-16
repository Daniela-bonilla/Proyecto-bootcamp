import re 

texto="Mi numero es 167823"
resultado=re.search(r'\d+',texto) #busca un numero
print(f"{texto} resultado : {resultado.group()}")
texto="Mi numero es 4567823"
resultado=re.search(r'\d+',texto) #busca un numero
print(f"{texto} resultado : {resultado.group()}")
