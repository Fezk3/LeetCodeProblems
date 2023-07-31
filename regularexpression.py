# make a regular expression that matches strings that end and begin with the same letter, the string is composed only of the character a and b

import re

regularExpression = r"^(a|b).\1$|^(a|b)$"
rg = "^[a-z]{3}[0-5]{3,5}[]$"
rg = "^[a-z]{3}[0-9]{3,5}[^a-zA-Z0-9]{1}[A-Z]{0,2}$"

def isAB(s):
    return re.search(rg, s) is not None

print(isAB("asd654%AA"))
print(isAB("asd654%"))
print(isAB("ab"))


