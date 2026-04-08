class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        allmapped = {}

        for m,n in enumerate(nums):
            diff = target - n

            if diff in allmapped:
                return [allmapped[diff], m]
            
            allmapped[n] = m

        

            
  
                
        
        