class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {} 
        dict2 = {}
        for element in s: 
            dict1[element] = dict1.get(element, 0) + 1
        
        for element in t: 
            dict2[element] = dict2.get(element, 0) + 1


        if dict1 == dict2: 
            return True
        else: 
            return False
        