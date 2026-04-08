class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = [i.lower() for i in s if i.isalnum()]
        return clean == clean[::-1]