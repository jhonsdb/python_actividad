""" is_integer(): Comprueba si el número de punto flotante tiene una parte decimal igual a cero. """
number = 5.0
is_integer = number.is_integer()  # True
print(is_integer)

""" max() y min(): Encuentran el valor máximo o mínimo entre varios números de punto flotante """

maxi = max(2.0, 4.5, 1.2)  # 4.5
print(maxi)
mini = min(-1.0, 0.0, 2.5)  # -1.0
print(mini)

""" math.sqrt(): Calcula la raíz cuadrada de un número de punto flotante. """
import math
square = math.sqrt(16.0)  # 4.0
print(square)
