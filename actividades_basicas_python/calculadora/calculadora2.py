number1 = int(input("Ingrese un numero:"))
number2 = int(input("Ingrese el segundo numero:"))

eleccion = 0

while eleccion !=6:
    print(""" 
    Indique la operacion a realizar 
    
    1 suma
    2 resta
    3 Multiplicacion
    4 Division
    5 Cambios de valores
    6 Salir
     """ )
    eleccion = int(input())

    if eleccion == 1:
        print(" ")
        print("Resultado ", number1,"+",number2,"=",number1+number2)
    if eleccion == 2:
        print(" ")
        print("Resultado ",number1,"-",number2,"=",number1-number2)
    if eleccion==3:
        print(" ")
        print("Resultado ",number1,"*",number2,"=", number1*number2)
    if eleccion==4:
        print(" ")
        print("Resultado ",number1,"/",number2,"=",number1/number2)
    if eleccion==5:
        number1 = int(input("Ingrese un numero:"))
        number2 = int(input("Ingrese el segundo numero:"))

    if eleccion == 6:
        print("ADIOS")    