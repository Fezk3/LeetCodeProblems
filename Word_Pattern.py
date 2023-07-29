def word_pattern(pattern, s):
    pals = s.split(" ")

    if len(pattern) != len(pals):
        return False

    lTP = {}
    pTL = {}

    for char, pal in zip(pattern, pals):
        if char in lTP and lTP[char] != pal:
            return False
        if pal in pTL and pTL[pal] != char:
            return False
        lTP[char] = pal
        pTL[pal] = char

    return True


print(word_pattern('abba', "cat dog dog cat"))
