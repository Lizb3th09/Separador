def load_sustantivo_sentimientos():
    fid = open("DB/Sustantivos.txt")
    sustantivo = dict()
    lista = list()
    sustantivo["sentimiento"]={}
    for line in fid:
        for l in line.split(','):
            lista.append(l)
    sustantivo["sentimiento"] = lista
    print(sustantivo)

    fid.close()
load_sustantivo_sentimientos()
