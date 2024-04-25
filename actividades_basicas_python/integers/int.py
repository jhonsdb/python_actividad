""" bit_length(): Devuelve el número de bits necesarios para representar el entero en binario, excluyendo el signo y los ceros iniciales. """
num = 42
bits = num.bit_length()

""" abs(): Devuelve el valor absoluto del entero. """
num = -10
absolute_value = abs(num)  
print(absolute_value)

""" round(): Redondea el entero a un número especificado de dígitos decimales (en este caso, a 0 dígitos decimales). """
num = 3.14159
redondeado = round(num) 
print(redondeado)

""" int(x): Convierte otro tipo de dato (como un float o una cadena) a un entero. """
numero_float = 3.14
convertido_a_entero = int(numero_float) 
print(convertido_a_entero)

""" bin(), oct(), hex(): Convierten el entero a su representación binaria, octal o hexadecimal, respectivamente. """
num = 42
binario = bin(num)  # '0b101010'
octal = oct(num)    # '0o52'
hexadecimal = hex(num)  # '0x2a
print(binario)
print(octal)
print(hexadecimal)

""" chr(): Convierte un entero en su representación de carácter Unicode. """
codigo_unicode = 65
caracter = chr(codigo_unicode)  # 'A'
print(caracter)

"""  ord(): Devuelve el valor Unicode del carácter. """
caracter = 'A'
unicode_valor = ord(caracter)  # 65
print(unicode_valor)

