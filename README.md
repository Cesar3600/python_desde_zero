
# **PYTHON DESDE ZERO**


## **POR QUE USAR PYTHON**

> [!IMPORTANT]
> A. facil de entender.
> B. facil de aprender.
> C. fácil de usar.
> D. uso de identacion.
> E. gran biblioteca standard de codigo para pdoer ser reutilizado.
> F. se pude mesclar con otros lenguajes de programacion.
> G. es multiplataforma, puede correr en cualquier sistema operativo (windows, linux y mac)
> H. es multiparadigma, se puede aplicar a mac, linux, windows.
> I. bien pagado.

***

## **QUE SE PUEDE HACER CON PYTHON**

A. desarrollar paginas webs del lado del servidor.
B. 2 frameworks : flask & django para desarrollar sitios webs.
C. aplicaciones moviles, desktop.
D. automatizacion.
E. ciencias de datos y machine learning.
F. desarrollo de software.
G. automatizacio de pruebas de software.
H. Se pueden crear juegos.

***

## **INSTALACION DE PYTHON**
> [!IMPORTANT]
> **DESCARGAR:**
> ir a https://www.python.org/downloads/
> descargar la ultima version

a. puedes buscar el interpreste de python (buscar python 3.10 o el que hallas instalado).
b. Usar en vs code.
c. Extensiones: python, prettier, python indent
d. el formato de python es .py

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

> [!INFO]
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
a. Conjunto de elementos.
b. No muestra datos duplicados.
c. No permite modificar los elementos internos.
d. A diferencia de las tuplas no permite acceder a los elementos del conjunto.
e. No permite repetir valores.
f. Para acceder a sus elementos se debe usar un bucle.
g. Son datos desordenados.

```py
#creando un conjunto (set)
conjunto = {'Delia','Catherine','Cesar',True,333}

#mal
conjunto[0] = 'Mal caracter'

#bien
conjunto = {"Aqui si deja modificar el conjunto"}
```

### DICCIONARIO
a. Utiliza { }.
b. Literalmente es un JSON.
c. Es una lista.
d. Muestra los datos por el nombre asociado.
e. Tiene una estructura key : value.

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
>**cuadro**
>|operador|comparacion|
>|:---|:---------------------|
>| == | es igual que         |
>| != | es distinto de       |
>| <  | es menor que         |
>| <= | es menor o igual que |
>| <  | es mayor que         |
>| >= | es mayor o igual que |

## **CONDICIONALES**



