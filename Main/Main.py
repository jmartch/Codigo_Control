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

# 🔹 Función para verificar si un código es un EAN-13
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

# 🔹 Función para verificar si un código es un ISIN
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

# 🔹 Funciones para calcular los dígitos de control
def calcular_isbn10(codigo):
    if len(codigo) != 9 or not codigo.isdigit():
        raise ValueError("El código debe tener 9 dígitos numéricos.")

    suma = sum(int(codigo[i]) * (10 - i) for i in range(9))
    resto = suma % 11
    digito_control = 11 - resto

    return 'X' if digito_control == 10 else str(digito_control)

def calcular_isbn13(codigo):
    if len(codigo) != 12 or not codigo.isdigit():
        raise ValueError("El código debe tener 12 dígitos numéricos.")

    suma = sum(int(codigo[i]) * (1 if i % 2 == 0 else 3) for i in range(12))
    resto = suma % 10
    digito_control = (10 - resto) % 10  # Si resto es 0, el dígito de control también debe ser 0

    return str(digito_control)
def calcular_ean13(codigo):
    if len(codigo) != 12 or not codigo.isdigit():
        raise ValueError("El código debe tener 12 dígitos numéricos.")

    suma = sum(int(codigo[i]) * (3 if i % 2 else 1) for i in range(12))
    digito_control = (10 - (suma % 10)) % 10

    return str(digito_control)


def calcular_isin(codigo):
    """Calcula el dígito de control de un código ISIN correctamente sin invertir el número"""
    if len(codigo) != 11:
        raise ValueError("El código debe tener 11 caracteres.")

    #  Convertir letras a números (A=10, ..., Z=35)
    isin = ""
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in codigo:
        if char.isdigit():
            isin += char
        elif char.isalpha():
            isin += str(abc.index(char) + 10)
        else:
            raise ValueError("El código ISIN solo puede contener letras y números.")

    suma = 0
    for i in range(len(isin)):
        num = int(isin[i])
        if i % 2 == 0:  # Posiciones impares en tu lógica
            doble = num * 2
            suma += (doble // 10) + (doble % 10) if doble >= 10 else doble
        else:  # Posiciones pares
            suma += num

    #  Obtener el dígito de control
    digito_control = (10 - (suma % 10)) % 10
    return str(digito_control)


# Menú principal
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
        while True:
            opcion_codigo = input("Opciones:\n"
                    "1. Código ISBN-10\n"
                    "2. Código EAN-13\n"
                    "3. Código ISIN\n"
                    "4. Código ISBN-13\n"
                    "5. Regresar\n")
        
            if opcion_codigo == "1":
                codigo = input("Ingrese los primeros 9 dígitos del ISBN: ")
                print(f"Dígito de control ISBN-10: {calcular_isbn10(codigo)}")

            elif opcion_codigo == "2":
                codigo = input("Ingrese los primeros 12 dígitos del EAN-13: ")
                print(f"Dígito de control EAN-13: {calcular_ean13(codigo)}")

            elif opcion_codigo == "3":
                codigo = input("Ingrese los primeros 11 caracteres del ISIN: ").upper()
                if len(codigo) != 11:
                    print("❌ Error: El código ISIN debe tener exactamente 11 caracteres.")
                else:
                    print(f"Dígito de control ISIN: {calcular_isin(codigo)}")
            elif opcion_codigo == "4":
                codigo = input("Ingrese los primeros 12 dígitos del ISBN: ")
                print(f"Dígito de control ISBN-13: {calcular_isbn13(codigo)}")

            elif opcion_codigo == "5":
                break  # Regresar al menú principal        
            else:
                print("Opción no válida. Intente de nuevo.")
    
    elif opcion == "5":
        w = True
        print("Gracias por usar DecodeTalker. ¡Hasta luego!")
    else:
        print("Opción no válida. Intente nuevamente.")


