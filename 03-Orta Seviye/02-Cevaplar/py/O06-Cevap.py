def ikilikten_onluga(ikilik):
    ikilik = ikilik[::-1]
    ondalık = 0
    for i in range(len(ikilik)):
        ondalık += ikilik[i] * 2**i
    return ondalık
    