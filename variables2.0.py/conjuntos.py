
conjunto = set(['dato 1','dato 2'])

print(conjunto) # {'dato 2', 'dato 1'}

#

conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}

print(conjunto2)#{frozenset({'dato2', 'dato1'}), 'dato3'}



#teoria de conjuntos

#issubset
conjuntonr1 = {1,3,5,7}
conjuntonr2 = {1,3,7}

resultado = conjuntonr2.issubset(conjuntonr1)
# o tambien resultado = conjuntonr2 <= conjuntonr1
print(resultado)


#issuperset
resultado = conjuntonr1.issuperset(conjuntonr2)
# o tambienn resultado = conjuntonr2 > conjuntonr1
print(resultado)


# verificar si hay algun numero en comun
resultado = conjuntonr2.isdisjoint(conjuntonr1)
print(resultado)

