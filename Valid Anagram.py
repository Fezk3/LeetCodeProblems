def anagram(s, t):

    if len(s) != len(t):
        return False

    pal1 = {}
    pal2 = {}

    for l, l2 in zip(s, t):
        if l in pal1:
            pal1[l] += 1
        else:
            pal1[l] = 1
        if l2 in pal2:
            pal2[l2] += 1
        else:
            pal2[l2] = 1

    for key in pal1.keys():
        if key not in pal2.keys():
            return False

    for key1, val1 in pal1.items():
        if val1 != pal2[key1]:
            return False
    return True

def easierAnagram(s,t):
    return sorted(s) == sorted(t)


print(easierAnagram(s = "anagram", t = "nagaram"))
print(anagram(s = "anagram", t = "nagaram"))

