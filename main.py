import mifuntion
import validador


if __name__ == '__main__':
    archivo_gramatica = open("gramatica.txt")
    if validador.valida_caracteres(archivo_gramatica):
        for linea in archivo_gramatica:
            for palabra in linea.split():
                token = mifuntion.find_sustantivos(palabra)
                #lprint(f"\t La palabra [{palabra}] -> {token}")
    else:
        print("Error revisa su texto")