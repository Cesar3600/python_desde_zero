
#if else

# se ejecuta por que la condicion es True
if 2 == 2:
  print("accion se ejecuta")

# No se ejecuta por que la condicion es False
if 2 != 2:
  print("accion NO se ejecuta")


edad = 9

if edad >= 18:
    print("Eres mayor de edad")
else:
    print('No eres mayor')
    
print("no forma parte de ninguna condicion")




#EJEMPLO:
#
panales = {
  'premium':{
    'precio':73.9,
    'cantidad':60
  },
  'confort':{
    'precio':62.9,
    'cantidad':48
  },
}

precio1 = panales['premium']['precio']
cant1   = panales['premium']['cantidad']
preunit1 = precio1/cant1

precio2 = panales['confort']['precio']
cant2   = panales['confort']['cantidad']
preunit2 = precio2/cant2




if preunit1 > preunit2:
  diference = preunit1 - preunit2
  print(f"PREMIUM es mas caro {preunit1} por {diference}")
  precio_total1 = preunit1 * cant1
  print(f"el precio total seria de {precio_total1} por {cant1}")
else:
  diference = preunit2 - preunit1
  print(f"COMFORT es mas caro {preunit2} por {diference}")
  precio_total2 = preunit2 * cant2
  print(f"el precio total seria de {precio_total2} por {cant2}")
  
  

ingreso_mensual = 72000
gasto_mensual = 80000

if ingreso_mensual > 10000:
  if ingreso_mensual - gasto_mensual < 3000:
    print("ahora si estas bien")
  else:
    print("muchos gastos")
elif ingreso_mensual > 1000:
  print("estas bien en latinoamerica")
elif ingreso_mensual > 500:
  print("esta bien en argentina")
elif ingreso_mensual > 200:
  print("estas bien en venezuela")
else:
  print("eres pobre")




