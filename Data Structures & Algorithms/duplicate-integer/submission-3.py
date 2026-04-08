class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = sorted(nums)
        for n in range(len(x)-1):
            if x[n] == x[n+1] :
                return True
            
        return False

         