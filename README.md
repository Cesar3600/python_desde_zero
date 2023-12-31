
# **PYTHON DESDE ZERO**


## **POR QUE USAR PYTHON**

> [!IMPORTANT]
> 1. facil de entender.
> 2. facil de aprender.
> 3. fácil de usar.
> 4. uso de identacion.
> 5. gran biblioteca standard de codigo para pdoer ser reutilizado.
> 6. se pude mesclar con otros lenguajes de programacion.
> 7. es multiplataforma, puede correr en cualquier sistema operativo (windows, linux y mac)
> 8. es multiparadigma, se puede aplicar a mac, linux, windows.
> 9. bien pagado.

***

## **QUE SE PUEDE HACER CON PYTHON**
>[!IMPORTANT]
> 1. desarrollar paginas webs del lado del servidor.
> 2. 2 frameworks : flask & django para desarrollar sitios webs.
> 3. aplicaciones moviles, desktop.
> 4. automatizacion.
> 5. ciencias de datos y machine learning.
> 6. desarrollo de software.
> 7. automatizacio de pruebas de software.
> 8. Se pueden crear juegos.

***

## **INSTALACION DE PYTHON**
> [!IMPORTANT]
> **DESCARGAR:**
> ir a https://www.python.org/downloads/
> descargar la ultima version

1. puedes buscar el interpreste de python (buscar python 3.10 o el que hallas instalado).
2. Usar en vs code.
3. Extensiones: python, prettier, python indent
4. el formato de python es .py

>[!NOTE]
>**RECUERDA**
>python es un lenguaje interpretado por lo tanto utiliza un inteprete. el inteprete de python es su consola. el itnerprete de python es diferente al cmd de window
>

***

## **DATOS SIMPLES**
de 4 tipos:
### **STRING**
para una linea: solo pueden emplearse en una sola linea:
"string" o
'string'

para varias lineas: 
```py
"""tus datos son:
    nombre:Lucas
    apellido: Hollander"""

'''tus datos son:
    nombre:Lucas
    apellido: Hollander'''
```
### **NUMEROS**
numeros enteros:
40

numeros en coma flotante:
40,2

### **BOOLEANO**
True
False

***

## **VARIABLES**
son espacios donde se almacenan valores de nuestro programa.

las variables no tienen un tipo definido por si mismos y dependiendo del valor asignado puede cambiar su comportamiento.
```py
a = 5
b = 8
c = a + b
print(c)
```

```py
nombre = "Hola mundo"
print(nombre)
```

```py
nombre = "cesar"
nombre = "delia"
nombre = "Catherine"
print(nombre)
```

**acumulador:**
```py
numero = 10
numero += 5
numero += 5
print(numero)
```

**concatenar:**
```py
nombre = 'Lucas'
bienvenida = 'Hola '+ nombre +' .Como estas?'
print(bienvenida)
```

**fstrings**
todo datos que le pasas a FString lo convertira a texto, aun asi le pases numbers, booleans 
```py
nombre = 'Micaela'
bienvenida = f"Hola {nombre}. Como estas?"
print(bienvenida)
```
**del**
se puede usar ***del*** para no definir una variable definida previamente.
```py
nombre = 'Micaela'
bienvenida = f"Hola {nombre}. Como estas?"
del bienvenida #eliminar la varible del scope global
print(bienvenida)
```

**pertenencia**
devolvera true ya que la palabra amo se encuentra en bienvenida.
```py
nombre = 'Delia'
bienvenida = f"Hola {nombre}. Te amo mi amor!"
print('amo' in bienvenida)
```

**anotaciones**
se puede usar # para u comentario que no se puede ver a no ser que estemos en la fuente del codigo.

```py
print("lucas" in bienvenida)      #true
print("lucas" not in bienvenida)  #false
```

**Tipos de anotacion de variables**

```py
nombre_de_hija = 'Mikaela'
bienvenida_a_hija = f"Hola {nombre}. mi todo!"
```

***

## **DATOS COMPUESTOS**

### **LISTA**
conjunto de elementos que pueden ser modificados
puedes mostrar la lista o un elemento colocando su index entre [ ]:

```py
lista = ['Delia','Catherine','Cesar',True,333]
print(lista)     #devuelve -> ['Delia', 'Catherine', 'Cesar', True, 333]

print(lista[1])  #devuelve -> Catherine

print(lista[2] = 'Arturo') #devuelve -> Arturo
```

> [!NOTE]
> **Para los iniciados**
> el index o la posicion empezando desde la izquierda siempre vale 0


### **TUPLA**
lista de elementos
no se puede modificar
utiliza ( ) para agrupar contenido

```py
#tupla
tupla = ('Delia','Catherine','Cesar',True,333)
print(tupla)

print(tupla[0])
#modificando tupla, no se puede modificar
tupla[0] = 'Maria'
print(tupla[0])
# Traceback (most recent call last):
#   File "c:\Users\cesar\Documents\practicas\python_desde_zero\datos-compuestos.py", line 15, in <module>
#     tupla[0] = 'Maria'
#     ~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
```

### CONJUNTO
1. Conjunto de elementos.
2. No muestra datos duplicados.
3. No permite modificar los elementos internos.
4. A diferencia de las tuplas no permite acceder a los elementos del conjunto.
5. No permite repetir valores.
6. Para acceder a sus elementos se debe usar un bucle.
7. Son datos desordenados.

```py
#creando un conjunto (set)
conjunto = {'Delia','Catherine','Cesar',True,333}

#mal
conjunto[0] = 'Mal caracter'

#bien
conjunto = {"Aqui si deja modificar el conjunto"}
```

### DICCIONARIO
1. Utiliza { }.
2. Literalmente es un JSON.
3. Es una lista.
4. Muestra los datos por el nombre asociado.
5. Tiene una estructura key : value.

```py
diccionario = {
  'nombre':"Delia Alva",
  'sexo':"Mujer",
  'emocionada':True,
  'altura':1.65
}

diccionario['nombre']  #devuelve Delia Alva 
```

## **OPERADORES ARITMETICOS**

### **suma & resta**
```py

suma = 12 + 5
print(suma)

resta = 12 - 5
print(resta)
```

### **multiplicacion & division**

```py
multiplicacion = 12 * 5 # 60
print(multiplicacion)

division = 12 / 5 # 2.4 devuelve float
print(division)
```
### **potenciacion y division baja**
```py
#potenciacion (exponente) (**)
exponente = 12**5
print(exponente) # 248832

#division baja
se refiere al entero de la division
division_baja = 12//5  # 2
print(division_baja)

```

### **modulo**
devuelve el resto
```py
modulo = 12%5  # 2
print(modulo)
```
### **exponente**
realiza exponenciacion
```py
exponenciacion = 2**3
print(exponenciacion) #8
```

### **tipo de dato**
```py
tipo_de_dato1 = type(["hola",12])
print(tipo_de_dato1) #list

tipo_de_dato2 = type(("hola",12))
print(tipo_de_dato2) #tuple

tipo_de_dato3 = type({"hola",12})
print(tipo_de_dato3) #set

tipo_de_dato4 = type({"nombre":"Cesar"})
print(tipo_de_dato4) #dict

```

***

## **OPERADORES DE COMPARACION**

>[!WARNING]
>**CUADRO**
>|operador|comparacion|
>|:---|:---------------------|
>| == | es igual que         |
>| != | es distinto de       |
>| <  | es menor que         |
>| <= | es menor o igual que |
>| <  | es mayor que         |
>| >= | es mayor o igual que |

```py

es_igual_que = 5 == 6  
print(es_igual_que)
#False

es_distinto_de = 5 != 6  
print(es_distinto_de)
#True

mayor_que = 5 > 6
print(mayor_que)
#False

menor_que = 5 < 6
print(menor_que)
#True

mayor_o_igual = 5 >= 6
print(mayor_o_igual)
#True

menor_o_igual = 5 <= 6
print(menor_o_igual)
#True

#ejemplo de comparacion
usuario_de_bd = 'Lucas'
usuario_escrito = 'peter'
print(usuario_de_bd == usuario_escrito)
```

***

## **CONDICIONALES**
ejecuta un codigo si se cumple una condicion:

```py

if edad > = 18:
    print("Eres mayor de edad")
else:
    print('No eres mayor')
```


## **OPERADORES LOGICOS**
>[!NOTE]
> OR, AND, NOT 

```py
#AND
resultado1 = True  & True   # devolver True
resultado2 = False & True   # devolver False
resultado3 = True  & False  # devolver False
resultado4 = False & False  # devolver False


#OR
resultado1 = True  | True   # devolver True
resultado2 = False | True   # devolver True
resultado3 = True  | False  # devolver True
resultado4 = False | False  # devolver False


#NOT
resultado = not True  | False  # devolver False
resultado = not False | False  # devolver True
```

***
## **METODOS DE CADENA**
dir muestra los metodos que podemos emplear en un string o cadena.

>[!NOTE]
>los metodos son funciones especificas de objetos
>No todas las funciones no son metodos

### **METODOS DE NUMBERS**

```py
cadena1 = "Hola soy Cesar"
cadena2 = "Bienvenido kaezar"
print(dir(cadena1))

""" ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'] """
```

### **METODOS DE NUMBERS**
```py
print(dir(4))

"""['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']"""
```

### **upper**
cambia el string a mayuscula

>[!NOTE]
>**formato**
>string.upper()
>

```py
cadena1 = "Hola soy Cesar" 
resultado = cadena1.upper() 
print(resultado)
#HOLA SOY CESAR
```

### **lower**
```py
resultado2 = cadena2.lower()
print(resultado2)
```

### **capitalize**
```py
resultado2 = cadena2.capitalize()
print(resultado2)
```
### **find**
busca una coincidencia y devuelve la primera posicion que encuentre.
si no encuentra devuelve -1

```py
busqueda_find = cadena1.find("a")
print(busqueda_find) # 3 por la posiciondonde encuentra la primera a

busqueda_find = cadena1.find("d")
print(busqueda_find) # -1 cuando no encuentra
```

### **index**
busca una coincidencia y devuelve la posicion, en caso que no encuentre te manda un excepcion
o sea que te manda error y detiene el proyecto.
```py
busqueda_index = cadena1.index("C")
print(busqueda_index) # 9 cuando no encuentra
```

### **isnumeric**
Devuelve true si un string contiene un numero. si no es un string devuelve excepcion

```py
numero = "123"
es_numerico = numero.isnumeric()
print(es_numerico) #True
```


### **isalpha**
si es falta numerico devuelve true

```py
alfanumerico = "hola123"
is_alpha = alfanumerico.isalpha()
print(is_alpha) #True
```
### **count**
Devuelve la cantidad de coincidencias

```py
texto_count = "hola mundo desde lima Peru"
count_elements = texto_count.count("a")
print(count_elements) #2
```
### **len**
no es un metodo, es una funcion.
Devuelve, cuenta la cantidad de caracteres de una cadena.

```py
texto_len = "hola mundo desde lima Peru"
count_elements = len(texto_len)
print(count_elements) #2
```
### **startswidth**
Es un metodo.
Devuelve booleano si encuentra que la cadena empieze con lo que se le indica.

```py
texto_startsWidth = "hola mundo desde lima Peru"
elements_startswidth = texto_startsWidth.startswidth("H")
print(elements_startswidth) #2
```
### **endswidth**
Es un metodo.
Devuelve booleano si encuentra que la cadena termine con lo que se le indica.

```py
texto_endsWith = "hola mundo desde lima Peru"
elements_endswith = texto_endsWith.endswith("h")
print(elements_endswith) 
```

### **replace**
1. Es un metodo.
2. Devuelve booleano si encuentra que la cadena empieze con lo que se le indica.
3. si no encuentra el texto a reemplazar simplemente no lo cambia
4. tiene 2 parametros: el primero reemplaza al segundo.

```py
cadena_nueva = "hola mundo! desde lima, Peru"
cadena_replace = cadena_nueva.replace("lima","amazonas")
print(cadena_replace) 
```
### **split**
1. Separa cadenas segun el elemento que le indiques
```py
cadena_nueva = "Hola mundo! desde lima, Peru"
cadena_split = cadena_nueva.split(",")
print(cadena_split) # ['hola mundo! desde Lima', ' Peru']
```

***

## **METODO DE LISTA**

>[!NOTE]
>***LAS TUPLAS Y LOS CONJUNTOS SON INMUTABLES***
>

>[!NOTE]
>***NO SE PUEDE USAR INDEX EN CONJUNTO ***


### **list**
Crea una lista
```py
lista = list("hola","dalto",34)
print(lista)
```
### **len**
Cuenta la gran cantidad de elementos de una lista.
```py
cadena = "hola"
longitud= len(cadena)
print(longitud)

# Cantidad de elementos con len
listaCantidad = len(["hola","dalto",34,True,"vida",12])
print(listaCantidad)
```

### **append**
1. Agrega un elemento en la lista.
2. no necesita que sea almacenado en una variable

```py
#append
lista = list(["hola","dalto",33,"Delia"])
lista.append("Mikaela")
print(lista)
```
### **insert**
Permite insertar un elemento dentro de una lista controlando la posicion donde se inserte.

```py
# insert
lista = list(["hola","dalto",33,"Delia"])
list_insert = lista.insert(2,"dato insertado")
print(list_insert)
```
### **extend**
Agrega varios elementos a la lista.
necesita que se le agregue una lista.

```py
#extends
listaExtend = list(["hola","Mikaela","Delia"])
listaExtend.extend([33,'tri',77,'soda stereo'])
print(listaExtend)
```
### **pop**
eliminar un elemento de la lista por su indice.

```py
#pop
listaExtend = list(["hola","Mikaela","Delia"])
listaExtend.pop(0)
print(listaExtend)

#eliminar el ultimo
listaExtend.pop(-1)
#eliminar el penultimo
listaExtend.pop(-2)
```

### **remove**
eliminar un elemento de la lista por su indice.
si no encuentra entonces manda excepcion

```py
#remove
listaExtend = list(["hola","Mikaela","Delia","otro"])
listaExtend.remove(3)
print(listaExtend)
```
### **clear**
Eliminar todos los elementos de la lista.

```py
#clear
listaClear= list(["hola","Mikaela","Delia","otro"])
listaClear.clear()
print(listaClear)
```
### **sort**
ordena numeros de una lista

```py
#sort
listaSort = list([12,33,True,34,56,False])
listaSort.sort(reverse=False)
print(listaSort)
```









***
## **METODO DE DICCIONARIO**
### **keys()**
devuelve las claves en un array.
```py
diccionario = {
  "nombre":"lucas",
  "apellido":"dalto",
  "subs":1000000,
}

claves = diccionario.keys()
print(claves) #dict_keys(['nombre', 'apellido', 'subs'])
```


### **get()**
devuelve el valor de una clave
podemos usar : diccionario("nombre") para obtener el valor de nombre
sin embargo, si no encuentra el dato mandara una excepcion
al contrario de get que si no encuentra devuelv e none

```py
diccionario = {
  "nombre"   : "lucas",
  "apellido" : "dalto",
  "subs"     : 1000000,
}

valor = diccionario.get("nombre")
print(valor) #lucas

diccionario = {
  0:"mirko",
  1:"novick",
  2:56,
}
valor = diccionario.get(1)
print(valor) #lucas
```


### **clear()**
Elimina todos los elementos.

```py
#clear
diccionario = ['elemento1','elemento2']
diccionario.clear()
print(diccionario)
```



### **pop()**
Elimina un elemento pasandole su index.

```py
diccionario = ['elemento1','elemento2']
diccionario.pop(1)
print(diccionario) #['elemento1']

diccionario = {
  "nombre"   : "Cesar",
  "apellido" : "Contreras",
  "edad"     : 46,
  "distrito" : "Independencia",
}
diccionario.pop("edad")
print(diccionario) #{'nombre': 'Cesar', 'apellido': 'Contreras', 'distrito': 'Independencia'}
```


### **items()**
itera el dict (diccionario)

```py

```

***

## **ENTRADA DE LOS DATOS INPUTS**
```py
# INPUTS
# pedirle un dato al usuario
nombre = input("cual es tu nombre:")
print(f"el nombre es {nombre}")

# cual es tu nombre: Cesar
# el nombre es Cesar

numero = 33
#convierto el numero a entero y l  multiplico por 2
resultado = int(numero) * 2
print(resultado)

#convierto el numero a flotante y l  multiplico por 2
numero = 27
resultado = float(numero) * 2
print(resultado)
```

***


### **VARIABLES 2.0**

## **DESEMPAQUETADO DE VARIABLES**
funciona solo si existe una cantidad de variabloes igual a la cantidad de elementos
en caso contrario mandara excepcion

sirve por ejemplo en funciones que nos devuelven tuplas, listas, ...

```py
datos = ("Katherine","Alva")

nombre,apellido = datos

print(nombre) #Katherine
print(apellido) #Alva
```


## **TUPLAS**
se puede crear la tupla de las 2 formas:

> [!NOTE]
> de deben crear cuando son datos de solo lectura,
> manejan mejor la memoria
> normalmente las listas al ser modificables guardan en dos lugares en memoria.
> primero modifican en un lugar y luego en el otro.
> en cambio las tuplas solo se guardan en un sitio haciendola inmutable
> 

```py
tupla = tuple(["datos1","datos2"])
print(tupla) #('datos1', 'datos2')

#tambien se puede crear : 
tupla2 = "datos1","datos2"
print(tupla2)
```
si quieres crear una tupla desde un solo elemento tiene que agregar una "," al final

```py
tupla3 = "dato1",
print(type(tupla3))
```

## **CONJUNTOS - SET**
Los datos dentro del conjunto no son modificables.

para crear un set necesitas un iterable


```py
conjunto = set(['dato 1','dato 2'])

print(conjunto) # {'dato 2', 'dato 1'}
```

Esto no se puede:
No se puede agregar un conjunto dentro de otro conjunto simplemente insertandolo.

```py
conjunto1 = {"dato1","dato2"}
conjunto2 = {conjunto1,"dato3"}
print(conjunto2) 
```

### **frozenset**
permite unir conjuntos o sets

```py
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}

print(conjunto2) #{frozenset({'dato2', 'dato1'}), 'dato3'}
```

> [!NOTE]
> La teoria de conjunto se aplica a la inteligencia artificial
> si tenemos 2 conjuntos:
>
> A = {a,b,c}
> B ={a,b,c,d,e,f}
> 
>quiere decir que B es un superconjunto de A
> quiere decir que A es un subconjunto de B


## **TEORIA DE CONJUNTOS**

### **issubset**
devuelve true o false dependiendo si es conjunto es un subconjunto de:

```py
#teoria de conjuntos
conjuntonr1 = {1,3,5,7}
conjuntonr2 = {1,3,7}

resultado = conjuntonr2.issubset(conjuntonr1)
print(resultado)
```

## **DICCIONARIO**

```py
# creando diccionarios con dict()
diccionario = dict(nombre="Cesar",apellido="Contreras")
print(diccionario) #{'nombre': 'Cesar', 'apellido': 'Contreras'}

# esta es otra manera de crear un diccionario
# {"nombre":"Cesar","apellido":"Contreras"}




```

### **fromkeys**
el primer valor es lo que vamos a interar
el segundo valor es lo que vamos a igualar

```py
diccionario = dict.fromkeys("ABCDE","VALOR") 
print(diccionario)
# {'A': 'VALOR', 'B': 'VALOR', 'C': 'VALOR', 'D': 'VALOR', 'E': 'VALOR'}
```

podriamos usar

```py
diccionario = dict.fromkeys(["nombre","apellido","suscriptores"]) 

print(diccionario)  #{'nombre': None, 'apellido': None}
print(diccionario['apellido'])  #None
```


## **BUCLE FOR**












