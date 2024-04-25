""" Creacion ded tupla """
tup = ("primer_valor", "segundo_valor", "tercer_valor")
print(tup)

""" creacion de tupla de un solo elemto """
tup = ("valor_único",)
print(tup)



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


"""  puedes crear una tupla y añadir valores nuevos además de la tupla original. """
algunos_animales = ("perro", "gato", "ratón", "serpiente", "caballo")
todos_los_animales = algunos_animales + ("hámster", "jirafa")
print(todos_los_animales)

""" Convertir una lista en tupla  """
lista_colores = ["azul", "rojo", "amarillo", "naranja"]
colores = tuple(lista_colores)
print(colores)
print(type(colores))

""" eliminar una tupla """

animales = ("perro", "gato", "ratón", "serpiente", "caballo")
del animales

""" Con index, puedes consultar el índice de un determinado valor.  """
animaless = ("perro", "gato", "ratón", "serpiente", "caballo")
indice = animaless.index("serpiente")
print("Índice de 'serpiente':", indice)
print("Tupla de animales:", animaless)

""" Con count, puedes consultar cuántas veces aparece un elemento dentro de una tupla  """


animales = ("perro", "gato", "ratón", "serpiente", "caballo")
cantidad_perros = animales.count("perro")
print("Cantidad de 'perro' en la tupla:", cantidad_perros)
print("Tupla de animales:", animales)


