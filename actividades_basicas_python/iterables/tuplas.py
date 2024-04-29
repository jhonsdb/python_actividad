""" Creacion ded tupla """
tup = ("primer_valor", "segundo_valor", "tercer_valor")
print(tup)

""" creacion de tupla de un solo elemto """
tup = ("valor_único",)
print(tup)

print("")


animales = ("perro", "gato", "ratón")

""" Valores numéricos: """
números = (4, 17, 39, 12)

""" Valores booleanos: """
booleanos = (False, False, True, False)
 
"""También puedes hacer una mezcla de diferentes tipos de datos: """
persona = ("Persona de ejemplo", "Max", 1974, True)


""" seleccionar elementos dentro de una tupla 

Si quieres consultar varios valores, procede de la siguiente manera: """
animales = ("perro", "gato", "ratón", "serpiente", "caballo")
print(animales[1:3])
print("")

""" Convertir una tupla de Python en lista """
animales = ("perro", "gato", "ratón", "serpiente", "caballo")
lista_animales = list(animales)  # Utilizar list() para convertir la tupla en una lista
lista_animales[2] = "elefante"  # Modificar el elemento en el índice 2
print(lista_animales)  # Imprimir la lista modificada
print("")



"""  puedes crear una tupla y añadir valores nuevos además de la tupla original. """
algunos_animales = ("perro", "gato", "ratón", "serpiente", "caballo")
todos_los_animales = algunos_animales + ("hámster", "jirafa")
print(todos_los_animales)
print("")

""" Convertir una lista en tupla  """
lista_colores = ["azul", "rojo", "amarillo", "naranja"]
colores = tuple(lista_colores)
print(colores)
print(type(colores))
print("")


""" eliminar una tupla """

animales = ("perro", "gato", "ratón", "serpiente", "caballo")
del animales
print("")


""" Con index, puedes consultar el índice de un determinado valor.  """
animaless = ("perro", "gato", "ratón", "serpiente", "caballo")
indice = animaless.index("serpiente")
print("Índice de 'serpiente':", indice)
print("Tupla de animales:", animaless)
print("")


""" Con count, puedes consultar cuántas veces aparece un elemento dentro de una tupla  """


animales = ("perro", "gato", "ratón", "serpiente", "caballo")
cantidad_perros = animales.count("perro")
print("Cantidad de 'perro' en la tupla:", cantidad_perros)
print("Tupla de animales:", animales)
print("")

