def sheet_cutting(w:int, h:int , p:dict):
    if w == 0 or h == 0:
        return 0

    r = [[0 for _ in range(w + 1)] for _ in range(h + 1)] # Skal lagre beste mulige kutt herfra

    for i in range(1, h+1):
        for j in range(1, w + 1):

            best = p.get(p[(j, i)], 0)

            # horisontal
            for k in range(1, i):
                best = max(best, r[k][j] + r[i-k][j])

            # vertikalt
            for k in range(1, j):
                best = max(best, r[i][k] + r[i][j-k])

            r[i][j] = best

    return r[h][w]

prices = {(1, 1): 1, (2, 1): 3, (1, 2): 3, (2, 2): 3}

print(sheet_cutting(2, 2, prices))

