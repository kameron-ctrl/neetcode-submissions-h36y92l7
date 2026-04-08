class Solution:
    def isPalindrome(self, s: str) -> bool:

        remove =""

        for i in s:
            if i.isalnum():
                remove += i.lower()
        return remove == remove[::-1]
        
        
        