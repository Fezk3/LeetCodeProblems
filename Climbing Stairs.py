# DP wtf!!!!!

def stair(n):
    uno, dos = 1, 1

    for i in range(n - 1):
        temp = uno
        uno = uno + dos
        dos = temp

    return uno
