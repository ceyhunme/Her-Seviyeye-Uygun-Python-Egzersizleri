def tekrarlanmayan(girdi):
    sonuc = list()
    for i in range(len(girdi)):
        if girdi.count(girdi[i]) == 1:
            sonuc.append(girdi[i])
    return sonuc