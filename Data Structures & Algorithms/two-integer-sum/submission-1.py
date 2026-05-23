class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}
        ans = []

        for i, num in enumerate(nums): 
            if num in compliment: 
                ans.append(compliment[num])
                ans.append(i)
                print(compliment[num], i)
            else: 
                compliment[target - num] = i
            
        return ans
                
