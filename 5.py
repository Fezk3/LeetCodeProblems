def getWho(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    winners = []
    for word in s:
        even_odd = {"even": 0, "odd": 0}
        if all(letter not in vowels for letter in word) or len([letter for letter in word if letter in vowels]) == 0:
            winners.append("Chris")
            continue
        for letter in word:
            if letter in vowels:
                even_odd["even"] += 1
            else:
                even_odd["odd"] += 1
        if even_odd["even"] % 2 == 0:
            winners.append("Chris")
        else:
            winners.append("Alex")
    return winners


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s_count = int(input().strip())

    s = []

    for _ in range(s_count):
        s_item = input()
        s.append(s_item)

    result = getWho(s)
    print(result)

    #fptr.write('\n'.join(result))
    #fptr.write('\n')

    #fptr.close()