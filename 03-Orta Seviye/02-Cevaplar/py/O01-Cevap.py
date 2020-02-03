def mehmet_wins(mehmet,semih):
    mehmetKazandıklari = 0
    if mehmet[0] > semih[2]: mehmetKazandıklari += 1
    if mehmet[1] > semih[0]: mehmetKazandıklari += 1
    if mehmet[2] > semih[1]: mehmetKazandıklari += 1
    return mehmetKazandıklari >= 2