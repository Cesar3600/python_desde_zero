
cadena1 = "Hola soy Cesar"

cadena2 = "Bienvenido kaezar"

#print(dir(cadena1))
#print(dir(4))

resultado = cadena1.upper()
print(resultado)

resultado2 = cadena2.lower()
print(resultado2)

resultado3 = cadena1.capitalize()
print(resultado3)

resultado4 = cadena2.capitalize()
print(resultado4)

busqueda_find = cadena1.find("oy")
print(busqueda_find) #3

busqueda_index = cadena1.index("C")
print(busqueda_index) # 9 cuando no encuentra

# si es numerico devuelve true sino devuelve false
numero = "123"
es_numerico = numero.isnumeric()
print(es_numerico)


alfanumerico = "ass"
is_alpha = alfanumerico.isalpha()
print(is_alpha) #True


texto_count = "hola mundo desde lima Peru"
count_elements = texto_count.count("a")
print(count_elements) # devuelve 2


texto_len = "hola mundo desde lima Peru"
count_elements = len(texto_len)
print(count_elements) #2


texto_startsWidth = "hola mundo desde lima Peru"
elements_startswidth1 = texto_startsWidth.startswith('h')     
elements_startswidth2 = texto_startsWidth.startswith('H')     
elements_startswidth3 = texto_startsWidth.startswith('hola')  
elements_startswidth4 = texto_startsWidth.startswith('Hola')  
print(elements_startswidth1) # devuelve True
print(elements_startswidth2) # devuelve false
print(elements_startswidth3) # devuelve True
print(elements_startswidth4) # devuelve False



texto_endsWith = "hola mundo desde lima Peru"

elements_endswith1 = texto_endsWith.endswith("h")
print(elements_endswith1) #False

elements_endswith2 = texto_endsWith.endswith("u")
print(elements_endswith2) #True



cadena_nueva = "hola mundo! desde Lima, Peru"
cadena_replace = cadena_nueva.replace("Lima","el Amazonas de san Martin")
print(cadena_replace) 



textSplit = "hola mundo! desde Lima, Peru"
string_split = textSplit.split(",")
print(string_split)      # devuelve una lista ['hola mundo! desde Lima', ' Peru']
print(string_split[0])   # devuelve una lista 'hola mundo! desde Lima'
print(string_split[1])   # devuelve una lista ' Peru'



#list
lista = list(["hola","dalto",34])
print(lista)

# Cantidad de elementos con len
textCantidad = len("hola")
print(textCantidad)

# Cantidad de elementos con len
listaCantidad = len(["hola","dalto",34,True,"vida",12])
print(listaCantidad)

#append
lista = list(["hola","dalto",33,"Delia"])
lista.append("Mikaela")
print(lista)

#insert
lista = list(["hola","dalto",33,"Delia"])
list_insert = lista.insert(2,"dato insertado")
print(list_insert)

#extend
listaExtend = list(["hola","Mikaela","Delia"])
listaExtend.extend([33,'tri',77,'soda stereo'])
print(listaExtend)

#pop
listaExtend = list(["hola","Mikaela","Delia","Cesar"])
listaExtend.pop(0)
print(listaExtend)
print(len(listaExtend))

#eliminar el ultimo
listaExtend.pop(-1)
print(listaExtend)

#eliminar el penultimo
listaExtend.pop(-2)
print(listaExtend)


listaFamilia = list(["Mikaela","Delia","Cesar","walli"])
listaFamilia.remove("walli")
print(listaFamilia)


listaClear= list(["hola","Mikaela","Delia","otro"])
listaClear.clear()
print(listaClear)


listaSort = list([12,33,True,34,56,False])
listaSort.sort(reverse=True)
print(listaSort) #[56, 34, 33, 12, True, False]

listaSort.sort(reverse=False)
print(listaSort) #[False, True, 12, 33, 34, 56]

listaSort.reverse()
print(listaSort) #[56, 34, 33, 12, True, False]











