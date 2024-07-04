def find_sustantivos(palabra):
    fid = open('DB/Catalogo.txt')
    for line in fid:
        data = line.split(':')#0-> token, 1->lista palabras        
        for db_string in data:
            if palabra in db_string:
                fid.close()
                return data[0]
    
    fid.close()