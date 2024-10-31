lista = []  # lista vacía
listal = ["Este es un texto"]  # Una lista con un elemento.
lista2 = ['Una cadena', 123]  # Una lista de dos elementos
lista3 = [1, 2, 3, 4.5, 'hola', 'a']  # Una lista de seis elementos

print(lista)
print(listal)
print(lista2)
print(lista3)

#LISTAS ENLAZADAS
lista5 = [0, 1, 2, 3]
lista6 = ["A", "B", "C"]
lista7 = [lista5, lista6]
print(lista7)
print(lista7[0])  # Muestra sola lista5
print(lista7[1])  # Muestra sola lista6
print(lista7[1][0])  # Muestra de la lista6 el elemento en el índice 0

#OPERACIONES CON LISTAS

# Concatenación
lista8 = ["A", "B", "C", "E"]
lista9 = [1, 2, 3, 4, 5]
lista10 = lista8 + lista9
print(lista10[2])  # Imprime el tercer elemento de lista10

# El método extend agrega una lista al final de otra lista, la operación afecta la lista invocante
nombres1 = ["Antonio", "Maria", "Mabel"]
nombres2 = ["Barry", "John", "Guttag"]
nombres3 = ["Barry", "John", "Guttag"]
nombres1.extend(nombres2)
print(nombres1)
print(nombres2)

# Repetir
lista11 = [1, 2, 3, 4, 5]
lista12 = lista11 * 3
print(lista12)  # Imprime la lista repetida

# Comparación
# Usando los operadores convencionales (<, <=, >, >=, ==, !=)
print(["Rojas", 123] < ["Rosas", 123])  # Compara listas
print(["Rosas", 123] > ["rosas", 123])   # Compara listas
print(["Rosas", 123] > ["Rosas", 23])    # Compara listas

# Es posible determinar si un elemento se encuentra en una lista
lista13 = ["cien", "años", "de", "soledad"]
if "de" in lista13:
    print("Si esta en la lista")
else:
    print("No esta en la lista")

# Iterando una lista
lista15 = ["hola", "amigos", "mios"]
for palabra in lista15:  # para cada palabra de la lista
    print(palabra, end=", ")  # parámetro end evita salto de línea