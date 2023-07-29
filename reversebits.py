
def rever32bitnumber(n: int) -> int:
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        res = res | (bit << (31 - i))
    return res


def rever32bitnumber2(n: int) -> int:
    bit = n.__str__()
    return int(bit[::-1])


