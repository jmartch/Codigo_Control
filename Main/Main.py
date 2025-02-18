#Actividad #1 Teoria de Codigo
#Juanangel Martinez
#Vivian Buelvas
#Librerias
from isbnlib import is_isbn10

#Funciones
# Documentacion funcion is_isbn-10
# https://pypi.org/project/isbnlib/
# Codigo ejemplo de como funciona de la misma libreria
# is_isbn10(isbn10like)
# Validates as ISBN-10.
# import the core functions you need
# from isbnlib import canonical, is_isbn10, is_isbn13

# isbn = canonical("978-0446310789")
# if is_isbn13(isbn):
#    ...
# ...
# Función para verificar si un código es un EAN-13

def is_ean13(codigo):
    if not codigo.isdigit() or len(codigo) != 13:
        return False

    even = 0
    odd = 0
    check_bit = int(codigo[-1])
    check_val = codigo[:-1]

    for i, n in enumerate(check_val):
        if i % 2 == 0:
            even += int(n)
        else:
            odd += int(n)

    return ((3 * odd) + even + check_bit) % 10 == 0


def is_isin(codigo):
    sum = 0
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    k1 = str(codigo[0])
    k2 = str(codigo[1])

    isin = str(int(abc.index(k1) + 10)) + str(int(abc.index(k2) + 10)) + codigo[2:]

    for i in range(1,15):
        if i % 2 == 0:
            sum += int(isin[i-1])
        else:
            if int(isin[i-1]) * 2 >= 10 :
                sum += (int(isin[i-1]) * 2) // 10 +  (int(isin[i-1])*2) % 10
            else:
                sum += (int(isin[i-1])) * 2

    if sum % 10 == 0:
        return True
    else:
        return False

#Variables ciclo iterativo
w= False
while not w:
    print("\nBienvenido a DecodeTalker")
    opcion = input("Opciones:\n"
                   "1. Verificación ISBN-10\n"
                   "2. Verificación EAN-13\n"
                   "3. Verificación ISIN\n"
                   "4. Determinar código de control\n"
                   "5. Salir\n")

    if opcion == "1":
        codigo = input("Ingrese el Código: ")
        print("El código ingresado es un ISBN-10" if is_isbn10(codigo) else "El código ingresado NO es un ISBN-10")

    elif opcion == "2":
        codigo = input("Ingrese el Código: ")
        print("El código ingresado es un EAN-13" if is_ean13(codigo) else "El código ingresado NO es un EAN-13")

    elif opcion == "3":
        codigo = input("Ingrese el Código: ")
        codigo_g = codigo.upper()
        is_isin(codigo_g)
        print("El código ingresado es un ISIN" if is_isin(codigo) else "El código ingresado NO es un ISIN")

    elif opcion == "4":
        codigo = input("Ingrese el Código a resolver: ")
        print(f"El dígito de control es: {calcular_digito_control(codigo)}")

    elif opcion == "5":
        w = True
        print("Gracias por usar DecodeTalker. ¡Hasta luego!")
    else:
        print("Opción no válida. Intente nuevamente.")


