#keys
diccionario = {
  "nombre":"lucas",
  "apellido":"dalto",
  "subs":1000000,
}

claves = diccionario.keys()
print(claves) #dict_keys(['nombre', 'apellido', 'subs'])



#get
diccionario = {
  "nombre":"lucas",
  "apellido":"dalto",
  "subs":1000000,
}
valor = diccionario.get("nombre")
print(valor) #lucas

diccionario = {
  0:"lucas",
  1:"dalto",
  2:1000000,
}
valor = diccionario.get(1)
print(valor) #lucas


#clear
diccionario = ['elemento1','elemento2']
diccionario.clear()
print(diccionario)


#pop
diccionario = ['elemento1','elemento2']
diccionario.pop(1)
print(diccionario) #['elemento1']


diccionario = {
  "nombre":"Cesar",
  "apellido":"Contreras",
  "edad":46,
  "distrito":"Independencia",
}

diccionario.pop("edad")
print(diccionario) #{'nombre': 'Cesar', 'apellido': 'Contreras', 'distrito': 'Independencia'}





