def vezir_kontrol(sütun,satır):
    tahta = [ [0]*8 for i in range(8) ]
    sütun, satır = ord(sütun) - 97, abs(satır - 8)
    
    for i in range(8):
        for j in range(8):
            if i == satır or j == sütun or abs(satır-i) == abs(sütun - j):
                tahta[i][j] = 1
    tahta[satır][sütun]=0
    return tahta