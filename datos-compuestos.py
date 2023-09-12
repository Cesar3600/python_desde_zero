
#Lista

lista = ['Delia','Catherine','Cesar',True,333]
print(lista)

print(lista[1])

#tupla
tupla = ('Delia','Catherine','Cesar',True,333)
print(tupla)
print(tupla[0])

#modificando tupla, no se puede
tupla[0] = 'Maria'
print(tupla[0])

#creando un conjunto (set)

conjunto = {'Delia','Catherine','Cesar',True,333}

#mal
conjunto[0] = 'Mal caracter'

#bien
conjunto = {"Aqui si deja modificar el conjunto"}


#diccionario
diccionario = {
  'nombre'    : "Delia Alva",
  'sexo'      : "Mujer",
  'emocionada': True,
  'altura'    : 1.65
}

print(diccionario['nombre'])


