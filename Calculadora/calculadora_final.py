
# TAREA 1 Creacion de una calculadora en PYTHON

#Solicitamos  que el usuario ingrese  dos nnumeros aleatorios
num1 = input("Favor de ingresar un numero cualquiera")
num2 = input("Favor de ingresar  el segundo  numero cualquiera")

#Covertimos las variables a de tipo flotante para que puedan aceptar  puntos decimales
num1 = float(num1)
num2 = float(num2)

#Aqui se realiza  la suma y se la mostramos al usuario
print("El resultado de tu suma es igual a", num1 + num2)

#Menu de opciones de la calculadora
print("MENU DE OPCIONES")
print(" Algunas  o5pciones de calculos que puede realizar esta calculadora:")
print("1. Restar el primer numero menos  el segundo numero")
print("2. Multiplicación")
print("3. División")
print("4. Reciduo")
print("5. Sumar tres números diferentes ")
print("6. Realizacion de operación multiples combinada entre Suma,Resta,Division y Multiplicacion")

op = input("Favor de eligir una opción de menu entre el  (1 y 6)  o simplemente  presiona Enter para terminar el proigrama  gracias: ")

if op == "1":
    print(" Usted a elegido la opcion de  la Resta:", num1 - num2)
elif op == "2":
    print("Usted a elegido la opcion de  laMultiplicación:", num1 * num2)
elif op == "3":
    if num2 != 0:
        print(" Usted ha elegido la opcion de  la  División:", num1 / num2)
    else:
        print("ERROR ERROR ERROR  La División es por cero")
elif op == "4":
    print("Usted a elegido la opcion de Residuo:", num1 % num2)
elif op == "5":
    # Sumar tres números
    num3 = input("Favor de ingresa un tercer número cualquiera: ")
    num3 = float(num3)
    print(" Se Realiza la suma de tres numeros:", num1 + num2 + num3)
elif op == "6":
    # Operación combinada simple
    expr = input("Favor de escribe una operación con 3  numeros o más  P/E  2 + 4 - 3: ")
    try:
        resultado = eval(expr)
        print("EL Resultado es:", resultado)
    except Exception as e:
        print("ERROR ERROR ERROR en expresión:", e)
else:
    print("No se realizaron más operaciones.")