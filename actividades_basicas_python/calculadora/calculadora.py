
""" 
(1) suma
(2) resta
(3) multiplicacion
(4) divison
"""

def calculadora(num1, num2, op):
    if op == 1:
        print (f"El resultado de la suma de {num1} y {num2}: {num1 + num2}")
    elif op == 2:
       print (f"El resultado de la resta de {num1} y {num2}: {num1 - num2}")
    elif op == 3:
        print (f"El resultado de la multiplicacion de {num1} y {num2}: {num1 * num2}")
    elif op == 4:
        print (f"El resultado de la division de {num1} y {num2}: {num1 / num2}")
    else:
        print("te equivocastes de opcion")

variable1= int(input("Introduzca su el primer valor"))
variable2= int(input("Introduzca su el segundo valor"))

calculadora(variable1,variable2,1)