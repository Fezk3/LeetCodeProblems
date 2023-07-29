# make a regular expression that matches strings that end and begin with the same letter, the string is composed only of the character a and b

import re

regularExpression = r"^(a|b).*\1$"

def isAB(s):
    return re.search(regularExpression, s) is not None

print(isAB("a"))
print(isAB("b"))
print(isAB("ab"))
print(isAB("ba"))
print(isAB("aba"))

