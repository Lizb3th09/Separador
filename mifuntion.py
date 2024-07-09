# Gramatica establecida 

gramatica = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
             'ñ','o','p','q','r','s','t','u','v','w','x','y','z',',','.',
             '¿','?','!','¡',':',';','á','é','í','ó','ú','ü','ö','ë','ä','ï',
             ' ','0','1','2','3','4','5','6','7','8','9']


# Función que analiza  si los caracteres están en la gramática

def analiza_caracteres(cadena):
    for caracter in cadena:
        if caracter.lower() not in gramatica:
            return f"Error,caracter invalido'{caracter}'"
    return ''

# Solicitar cadena de texto al usuario
#cadena_usuario = input("Ingrese una cadena de texto: ")
#caracteres_no_aseptados = analiza_caracteres(cadena_usuario)


# Funcion que busca si las palabras estan en nuestro catalogo

def find_sustantivos(palabra):
    with  open('DB/Catalogo.txt', encoding='utf-8') as fid:
        for line in fid:
            data = line.split(':')     
            for db_string in data:
               if palabra in db_string:
                   return int(data[0]), data        
    return 0,' '


#Analiza y valida el archivo gramatica.txt

with open('gramatica.txt', 'r', encoding='utf-8') as file:
     cadena_usuario = file.read().strip()
caracteres_no_aseptados = analiza_caracteres(cadena_usuario)



# Lista de tokens

if caracteres_no_aseptados:
    print(caracteres_no_aseptados)
else:
    lista_tokens = []
    for componente in cadena_usuario.split():
        token, data = find_sustantivos(componente)
        print(f"\tLa palabra: {componente} -> {token}")
        lista_tokens.append(token)
    print(lista_tokens)