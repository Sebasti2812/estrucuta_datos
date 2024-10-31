tuplal = () # Tupla vacía
print(tuplal)
tupla2 = ("Esto es un texto",) # Una tupla con un elemento que es una cadena
print(tupla2)
tupla3 = ("Una cadena", 123) # Una tupla con dos elementos
print(tupla3)
tupla4 = ("apple", 2018, "samsung", 4.9, "t", True) # Una tupla de seis elementos
print(tupla4)

#ELEMENTOS DE UNA TUPLA

tupla3 = (2, 4.7, "nota", 5, 3, 2.9)
print(tupla3[1])
print(tupla3[2])
print(tupla3[3])

#TUPLAS ENLAZADAS
tupla5 = (0, 1, 2, 3)
tupla6 = ("A", "B", "C")
tupla7 = (tupla5, tupla6)
print(tupla7)
print(tupla7[0])  # Muestra solo la tupla 1
print(tupla7[1])  # Muestra solo la tupla 2
print(tupla7[1][0])  # Muestra de la tupla 2 el elemento en el índice 0


#OPERACIONES CON TUPLAS

# Concatenar
tupla8 = ("A", "B", "C", "E")
tupla9 = (1, 2, 3, 4, 5)
tupla10 = tupla8 + tupla9
print(tupla10)

# Repetir
# Crea una tupla con múltiples copias de una tupla.
tupla11 = (1, 2, 3, 4, 5)
tupla12 = tupla11 * 3
print(tupla12)

# Comparar
# Se usan los operadores convencionales (<, <=, >, >=, ==, !=)
tupla13 = ("Rojas",)
tupla14 = (123,)
tupla15 = ("Rosas",)
tupla16 = ("rosas",)

print((tupla13, tupla14) < (tupla15, tupla14))
print((tupla15, tupla14) == (tupla16, tupla14))