""" Deveuelve la longitud de la cadena """
string = "Hello, world!"
length = len(string)
print(length)
print("")

""" upper() y lower()  Convierten la cadena a mayúsculas o minúsculas, respectivamente.
"""
string ="hola"
upper=string.upper()
print(upper)

string ="COMO ESTAS"
lower=string.lower()
print(lower)
print("")

""" capitalize() y title(): capitalize() convierte el primer carácter a mayúsculas, y title() convierte el primer carácter de cada palabra a mayúsculas.
 """

string = "primera paralabra"
capitalize=string.capitalize()
print(capitalize)

string ="segunda palabra"
with_title=string.title()
print(with_title)
print("")

""" count(subcadena): Cuenta cuántas veces aparece una subcadena en la cadena. """

string = "tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres."
count = string.count("tres")
print(count)
print("")

""" find(subcadena) y index(subcadena): Encuentran la posición de la primera aparición de una subcadena. La diferencia es que find() devuelve -1 si no encuentra la subcadena, mientras que index() genera una excepción ValueError. """

string = "Hola a todos espero que tengan un buen dia"
positio1 = string.find("tengan")
position2 = string.index("H")

print(positio1)
print (position2)

print("")

""" replace(viejo, nuevo): Reemplaza todas las ocurrencias de la subcadena vieja con la nueva.
 """

string = "Hello, world!"
new_string = string.replace("world", "Python")
print(new_string)
print("")

"""  strip(), lstrip(), y rstrip(): Eliminan espacios en blanco al principio, al final o en ambos extremos de la cadena, respectivamente.replace(search, replace): Reemplaza la primera ocurrencia de una subcadena con otra """

string= "          espacio en ambos lados                 "
without_spaces = string.strip()
print(without_spaces)

string ="espacial al final            "
without_space2=string.lstrip()
print(without_space2)

string = "espacio en ambos lados espacio al princoio             "
without_space3=string.rstrip()
print(without_space3)

print("")

""" startswith(prefijo) y endswith(sufijo): Comprueban si la cadena comienza o termina con el prefijo o sufijo dado, respectivamente """

string = "Hello, world!"
starts_with_hello = string.startswith("Hello")
ends_with_world = string.endswith("world!")
print(starts_with_hello)  
print(ends_with_world)    

print("")
""" split(separador): Divide la cadena en una lista de subcadenas utilizando el separador especificado. """

string = "Hello, world!"
parts = string.split(", ")
print(parts)  
print("")

""" join(iterable): Concatena las cadenas de un iterable utilizando la cadena como separador. """
words = ['Hello', 'world!']
string = ', '.join(words)
print(string)
 




