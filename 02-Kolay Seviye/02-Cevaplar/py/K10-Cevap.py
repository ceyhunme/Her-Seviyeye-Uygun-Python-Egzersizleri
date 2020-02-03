def gun(ay,yıl):
    gunler = {1:31,
             2:28,
             3:31,
             4:30,
             5:31,
             6:30,
             7:31,
             8:31,
             9:30,
             10:31,
             11:30,
             12:31}
    
    if ay == 2:
        if yıl % 4 == 0:
            if yıl % 100 == 0:
                if yıl % 400 == 0:
                    return 29
                return 28
            return 29
        return 28
    
    return gunler[ay]