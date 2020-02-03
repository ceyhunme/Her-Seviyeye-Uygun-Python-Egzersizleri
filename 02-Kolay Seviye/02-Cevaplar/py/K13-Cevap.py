def ortanca(yazi):
    if len(yazi) % 2 == 0:
        return yazi[len(yazi)//2 -1 : len(yazi)//2 + 1]
    return yazi[len(yazi)//2]