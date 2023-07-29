def isPalindrome(x):
    if x < 0:
        return False
    str = x.__str__()
    if str == str[::-1]:  # comparacion de string con string invertido
        return True
    return False

print(isPalindrome(212))