class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check length
        if len(s) != len(t):
            return False 

        # use one dict 
        count = {}

        for i in range(len(s)): 
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1
            # cumulatively, never have any elements if its anagram 

        for k,v in count.items():
            if v != 0:
                return False 

        return True

        