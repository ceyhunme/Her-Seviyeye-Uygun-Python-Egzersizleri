def dik_açılı(x,y,z):
    if x> 0 and y > 0 and z > 0:
        if x**2+y**2==z**2 or x**2 + z**2==y**2 or y**2+z**2==x**2:
            return True
        else:
            return False
    else:
        return False
        