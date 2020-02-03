def arkadas(liste):
    if liste.index("Vural") == liste.index("Fatih")+1:
        return True
    if liste.index("Vural") == liste.index("Fatih")-1:
        return True
    return False