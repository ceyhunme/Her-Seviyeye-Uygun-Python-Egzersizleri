def perrin(n):
    per = [3,0,2]
    if n == 0 or n == 1 or n == 2:
        return per[n]
    for i in range(3,n+1):
        per.append(per[i-2]+per[i-3])
    return per[n]