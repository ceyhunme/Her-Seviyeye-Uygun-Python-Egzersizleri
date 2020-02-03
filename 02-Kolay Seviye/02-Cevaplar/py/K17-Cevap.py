def apocalyptic(sayi):
    x = str(pow(2,sayi))
    if x.count("666") == 0:
        return "Güvenli"
    elif x.count("666") == 1:
        return "Tek"
    elif x.count("666") == 2:
        return "Çift"
    elif x.count("666") == 3:
        return "Üçlü"