def carpan(n):
    carp = 1
    for i in str(n):
        carp *= int(i)
    return carp

def çarpan_devamlılığı(n):
    işlem = 0
    while n > 9:
        n = carpan(n)
        işlem += 1
    return işlem