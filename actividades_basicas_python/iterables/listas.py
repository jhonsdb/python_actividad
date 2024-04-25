""" append(elemento): Agrega un elemento al final de la lis """
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
# Result: [1, 2, 3, 4]

""" extend(iterable): Agrega los elementos de un iterable (como otra lista) al final de la lista. """
my_list_1 = [1, 2, 3]
my_list_2 = [4, 5, 6]
my_list_1.extend(my_list_2)
print(my_list_1)
# Result: [1, 2, 3, 4, 5, 6]

""" insert(posición, elemento): Inserta un elemento en una posición específica de la lista. """
my_list = [1, 2, 3]
my_list.insert(3, 4)
print(my_list)
# Result: [1, 2, 3, 4]

""" pop([índice]): Elimina y devuelve el elemento en la posición dada (o el último si no se proporciona índic """
my_list = [1, 2, 3]
element = my_list.pop(1)
# Result: element = 2, my_list = [1, 3]

""" index(elemento[, inicio[, fin]]): Devuelve el índice de la primera aparición del elemento en la lista. Puedes especificar un rango opcional de búsqueda. """
my_list = [1, 2, 3, 4, 5, 2, 6, 7, 8, 9, 10]
index = my_list.index(2,2)
print(index)
# Result: index

""" count(elemento): Cuenta cuántas veces aparece el elemento en la lista. """
my_list = [1, 2, 3, 2]
occurrences = my_list.count(2)
print(occurrences)
# Result: occurrences=2

""" -sort(): Ordena la lista in-place (modifica la lista original """
my_list = [3, 1, 4, 1, 5, 9, 2]
my_list.sort()
print(my_list)
# Result: my_list=[1, 1, 2, 3, 4, 5, 9]

""" reverse(): Invierte el orden de los elementos en la list """
my_list = [1, 2, 3]
my_list.reverse()
# Result: my_list=[3, 2, 1

""" copy() o [:]: Crea una copia superficial de la lista. """
original_list = [1, 2, 3]
copy1 = original_list.copy()
copy2 = original_list[:]
print(copy2)
# Result: copy1=[1, 2, 3], copy2=[1, 2, 





