def sudoku_mu(sudoku):
    toplam = 0
    
    for kutu in sudoku:
        for eleman in kutu:
            if eleman < 1 or eleman >9:
                return False
            toplam += eleman
    return toplam == 45

def sudoku_mu2(sudoku):
    sudoku = [i for x in sudoku for i in x]
    return sorted(sudoku) == [1,2,3,4,5,6,7,8,9]