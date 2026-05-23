class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}

        for i, num in enumerate(nums): 
            if num in compliment: 
                return [compliment[num], i]
            else: 
                compliment[target - num] = i

                
