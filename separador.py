""" Que pueda separar  A-z,incluyendo Digitos de puntacion,letras con signo y numeros."""

import string


def caracter_valido():
    """Funcion para aseptar tipos de caracteres"""
    caracteres_validos=string.ascii_letters + string.digits + string.punctuation + "áéíóúÁÉÍÓÚÑñüÜ"
    return caracteres_validos

def separar_por_caracteres(cadena):
    """"Funcion que separa la cadena"""
    return list(cadena)

cadena_usuario = input("Ingrese una cadena de texto:")

caracteres_separados = separar_por_caracteres(cadena_usuario)
print("Cadena separada por caracteres:", caracteres_separados)
