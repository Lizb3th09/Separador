# Lizbeth Barcenas Mancilla

"""Separador de cadenas,que valide solo caracteres de nuestro lenguaje """

gramatica = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
             'ñ','o','p','q','r','s','t','u','v','w','x','y','z',',','.',
             '¿','?','!','¡',':',';','á','é','í','ó','ú','ü','ö','ë','ä','ï',
             ' ','0','1','2','3','4','5','6','7','8','9']

def separar_por_caracteres(cadena):
    """Función que separa la cadena si todos los caracteres están en la gramática"""
    for caracter in cadena:
        if caracter.lower() not in gramatica:
            return f"Error,caracter invalido'{caracter}'"
    return cadena.split()

cadena_usuario = input("Ingrese una cadena de texto: ")

caracteres_separados = separar_por_caracteres(cadena_usuario)
print("Cadena separada por caracteres: ", caracteres_separados)
