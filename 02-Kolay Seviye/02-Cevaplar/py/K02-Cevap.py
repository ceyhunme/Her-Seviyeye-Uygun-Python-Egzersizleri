def ayni_mi(yazi):
    if yazi.isupper():
        return True
    elif yazi.islower():
        return True
    else:
        return False
    
ayni_mi2 = lambda yazi2 : yazi2.isupper() or yazi2.islower()