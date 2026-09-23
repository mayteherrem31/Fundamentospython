# Creación de lista unidimensional
frutas = ["manzana", "banana", "cereza", "durazno"]
print("Lista original:", frutas)

# Acceso por índice
print("\nAccediendo a elementos:")
print("Primera fruta:", frutas[0])   # manzana
print("Última fruta:", frutas[-1])  # durazno

# Modificación por índice
frutas[1] = "pera"
print("\nDespués de modificar el segundo elemento:", frutas)

# Métodos básicos
frutas.append("uva")  # Agrega al final
print("\nDespués de append('uva'):", frutas)

frutas.insert(2, "kiwi")  # Inserta en posición 2
print("Después de insert(2, 'kiwi'):", frutas)

frutas.remove("cereza")  # Elimina por valor
print("Después de remove('cereza'):", frutas)

# Operaciones con listas
verduras = ["zanahoria", "espinaca"]

lista_compra = frutas + verduras  # Concatenación
print("\nLista de compras (concatenación):", lista_compra)

lista_repetida = verduras * 2  # Repetición
print("Lista repetida:", lista_repetida)
