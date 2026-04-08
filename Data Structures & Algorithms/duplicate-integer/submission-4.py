class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = sorted(nums)

        for i in range(len(x)-1):
            if x[i] == x[i+1]:
                return True

        return False