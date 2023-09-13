
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

***
## **METODO DE LISTA**
***
## **METODO DE DICCIONARIO**
***
## **ENTRADA DE LOS DATOS INPUTS**
***