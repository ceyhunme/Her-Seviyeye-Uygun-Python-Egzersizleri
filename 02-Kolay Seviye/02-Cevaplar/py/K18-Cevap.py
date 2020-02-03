def zip(yazi):
    sayılan =yazi.count("zip")
    if sayılan < 2:
        return -1
    else:
        ilk = yazi.find("zip")
        return yazi.find("zip",ilk+1)