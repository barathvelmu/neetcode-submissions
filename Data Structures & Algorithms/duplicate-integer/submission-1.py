class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        final_list = set()
        for element in nums: 
            if element in final_list: 
                return True 

            final_list.add(element)

        return False