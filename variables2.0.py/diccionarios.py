
# creando diccionarios con dict()
diccionario = dict(nombre="Cesar",apellido="Contreras")
print(diccionario) #{'nombre': 'Cesar', 'apellido': 'Contreras'}

#{"nombre":"Cesar","apellido":"Contreras"}


diccionario = dict.fromkeys("ABCDE","VALOR") 
print(diccionario)
# {'A': 'VALOR', 'B': 'VALOR', 'C': 'VALOR', 'D': 'VALOR', 'E': 'VALOR'}


#esto se evita asi:
diccionario = dict.fromkeys(["nombre","apellido","suscriptores"]) 

print(diccionario)  #{'nombre': None, 'apellido': None}
print(diccionario['apellido'])  #None




