class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        for num in nums: 
            dup = nums.copy()
            dup.remove(num)

            total = 1
            for element in dup:
                total *= element
            final.append(total)

        
        return final