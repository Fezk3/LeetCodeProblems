'''

 2 punteros uno al inicio otro al final
 comparan sus sumas al target
 si es mayor el puntero de la derecha decrementa
 si es menor el puntero de la izquierda aumenta
 asi hasta  que se encuentre el resultado y se retornan
 los indices+1

 linear -> O(n)

'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len((numbers)) - 1

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l+1,r+1]