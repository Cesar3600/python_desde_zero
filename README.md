
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





