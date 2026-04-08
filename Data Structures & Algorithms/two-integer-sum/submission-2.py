class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}

        for n,m in enumerate(nums):
            diff = target - m

            if diff in prevmap:
                return [prevmap[diff], n]
            
            prevmap[m] = n
            

                
        
        