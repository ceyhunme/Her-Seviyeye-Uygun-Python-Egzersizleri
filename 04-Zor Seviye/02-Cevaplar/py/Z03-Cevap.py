def tamamlanır_mı(ilk,kelime):
    depo = list(ilk)[::-1]
    for harf in kelime:
        if harf == depo[-1]: depo.pop()
    return not depo