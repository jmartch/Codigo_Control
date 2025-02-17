#Actividad #1 Teoria de Codigo
#Juanangel Martinez
#Vivian Buelvas
#Librerias
from idlelib.configdialog import is_int
import re
import isbnlib as isbn
from isbnlib import is_isbn10
import pandas as pd
#Variables ciclo iterativo
w = False

while(w != True):
    print("Bienvenido a DecodeTalker")
    opcion = int(input("Opciones "
          "1. Verificacion ISBN-10"
          "2. Verificacion EAN-13"
          "3. Verificacion ISIN"
          "4. Deteminar codigo de control"
          "5. Salir"))

    if (opcion == 1):
        codigo= int(input("Ingrese el Codigo "))

        if(is_isbn10(codigo)):
            print("El codigo ingresa es un EAN-13")
        else:
            print("El codigo ingresa NO es un EAN-13")
    if (opcion == 2):
        codigo = int(input("Ingrese el Codigo "))
        is_ean13(codigo)
    if (opcion == 3):
        codigo = int(input("Ingrese el Codigo "))
        if (identificador(codigo)):
            print("El codigo ingresa es un ISBN-10")
        else:
            print("El codigo ingresa NO es un ISIN")
    if (opcion == 4):
        codigo = int(input("Ingrese el Codigo a resolver "))
        c = identificador(codigo)
    if (opcion == 5):
        w = True

    def is_ean13(codigo):
        ean=codigo
        even = 0
        odd = 0
        check_bit = ean[len(ean) - 1]  # get check bit(last bit)
        check_val = ean[:-1]  # Get all vals except check bit

        if len(ean) != 13:  # Check the input length
            print("Invalid EAN 13")
        else:
            for index, num in enumerate(check_val):  # Gather Odd and Even Bits
                if (index % 2 == 0):
                    even += int(num)
                else:
                    odd += int(num)
            if (((3 * odd) + even + int(check_bit)) % 10 == 0):  # Check if the algorithm 3 * odd parity + even parity + check bit matches
                print("Valid EAN 13")
            else
                print("Invalid EAN 13")

    def is_isin(codigo):
        # Regex to check valid ISIN Code
        regex = "^[A-Z]{2}[-]{0, 1}[0-9A-Z]{8}[-]{0, 1}[0-9]{1}$"

        # Compile the ReGex
        p = re.compile(regex)

        # If the string is empty
        # return false
        if (codigo == None):
            return False

        # Return if the string
        # matched the ReGex
        if (re.search(p, codigo)):
            return True
        else:
            return False

    def resolver(codigo):
