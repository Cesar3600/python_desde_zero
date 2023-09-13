
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




