""" bit_length(): Devuelve el número de bits necesarios para representar el entero en binario, excluyendo el signo y los ceros iniciales. """
num = 42
bits = num.bit_length()
print("")

""" abs(): Devuelve el valor absoluto del entero. """
num = -10
absolute_value = abs(num)  
print(absolute_value)
print("")

""" round(): Redondea el entero a un número especificado de dígitos decimales (en este caso, a 0 dígitos decimales). """
num = 3.14159
redondeado = round(num) 
print(redondeado)
print("")

""" int(x): Convierte otro tipo de dato (como un float o una cadena) a un entero. """
numero_float = 3.14
convertido_a_entero = int(numero_float) 
print(convertido_a_entero)
print("")

""" bin(), oct(), hex(): Convierten el entero a su representación binaria, octal o hexadecimal, respectivamente. """
num = 42
binario = bin(num)  # '0b101010'
octal = oct(num)    # '0o52'
hexadecimal = hex(num)  # '0x2a
print(binario)
print(octal)
print(hexadecimal)
print("")

""" chr(): Convierte un entero en su representación de carácter Unicode. """
codigo_unicode = 65
caracter = chr(codigo_unicode)  # 'A'
print(caracter)
print("")
"""  ord(): Devuelve el valor Unicode del carácter. """
""" Unicode es un sistema de codificación de caracteres utilizado por los equipos informáticos
 para el almacenamiento y el intercambio de datos en formato de texto. """
caracter = 'A'
unicode_valor = ord(caracter)  # 65
print(unicode_valor)
print("")
