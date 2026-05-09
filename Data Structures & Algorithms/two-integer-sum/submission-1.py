class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} 

        for i in range(len(nums)): 
            needed = target - nums[i] # never neg cuz target > nums[i]

            if needed in seen: # checks the key 
                return [seen[needed], i] # cuz seen i < curr i 

            seen[nums[i]] = i

        return None


