

#el metodo extend agrega una lista al final de otra lista, la operacion afecta la lista invocante
nombres1 = ['Antonio', 'Maria', 'Mabel']
nombres2 = ['Barry', 'John', 'Guttag']
nombres1.extend(nombres2)
print(nombres1)
print(nombres2)

#repetir
lista10 = [1, 2, 3, 4, 5]
lista11 = lista10*3
print(lista11)

#comparacion
#usando los operadores convencionales(<, <=, >, >=, ==, !=)
print(['Rojas', 123] < ['Rosas', 123])
print(['Rosas', 123] == ['rosas', 123])
print(['Rosas', 123] > ['Rosas', 23])

#Es posible determinar si un elemento se encunetra en una lista
lista12 = ['cien', 'años', 'de', 'soledad']
if 'de' in lista12:
    print('Si esta en la lista')
else:
    print('No esta en la lista')

#Iterando una lista
lista13 = ['hola', 'amigos', 'mios']
for palabra in lista13: #para cada palabra de la lista
    print(palabra, end=',') # end evita salto de linea

#diccionarios
diccionario = {} #diccionario vacio
# diccionario con 4 items
puertos = {
    22:'SSH',
    23:'Telnet',
    80:'HTTP',
    3306:'MySQL'
}
print(puertos)

#El metodo update agrega items de un diccionario en otro
puertos1 = {
    22:'SSH',
    80:'HTTP'
}
puertos2 = {
    53:'DNS',
    443:'HTTPS'
}
print(puertos1)
puertos1.update(puertos2)
print(puertos1)

#Comparar
#Se mira si los diccionarios tienen los mismos items
a = {123:'Rojas', 87:'Rosas'} == {87:'Rosas', 123:'Rojas', 78:'Otro'}
print(a)

#Accediendo al valor de un item con la clave dada
puertos3 = {
22:"SSH",
    23:"Telnet",
    80:"HTTP",
    3306:"MySQL"
}
protocolo = puertos3[22]
print(protocolo)
#puertos3[8080]#Error

#Eliminar item con la clave dada
calificaciones = {
    "alumnos1":5,
    "alumnos2":3,
    "alumnos3":4,
    "alumnos4":3
}
print(calificaciones)
del calificaciones ["alumnos3"]
print(calificaciones)

#Iterar un diccionario
#usar el ciclo for y el metodo items para obtener los items de un diccionario.
dicPuertos = {
    22:"SSH",
    23:"Telnet",
    80:"Http"
}
for x,y in dicPuertos.items():
    print(x, "->", y)