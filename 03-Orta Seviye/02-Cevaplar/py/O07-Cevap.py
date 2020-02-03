def evreka(liste):
    for sayı in liste:
        if "7" in str(sayı):
            return "Boom!"
    return "listede 7 yok"