def countNumbers(arr):
    for i in arr:
        count = 0
        sublist = i
        for j in range(sublist[0], sublist[-1] + 1):
            if len(set(str(j))) == len(str(j)):
                count += 1
        print(count)

if __name__ == '__main__':

    arr_rows = int(input().strip())
    arr_columns = int(input().strip())

    arr = []

    for _ in range(arr_rows):
        arr.append(list(map(int, input().rstrip().split())))

    countNumbers(arr)

'''    count = 0
        unique_digits = set()
        for i in arr:
            sublist = i

            for j in range(sublist[0], sublist[-1] + 1):
                has_duplicate = False
                temp = j
                while temp > 0:
                    digit = temp % 10
                    if digit in unique_digits:
                        has_duplicate = True
                        break
                    unique_digits.add(digit)
                    temp //= 10
                if not has_duplicate:
                    count += 1
                unique_digits.clear()
            print(count)
            count = 0'''
