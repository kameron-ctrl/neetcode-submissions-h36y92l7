class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = sorted(s)
        y = sorted(t)

        lista = list(x)
        listb = list(y)

        if lista == listb:
            return True
        else: 
            return False
        