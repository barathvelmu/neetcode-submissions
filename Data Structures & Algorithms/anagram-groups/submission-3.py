class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} 

        for word in strs: 
            identity = ''.join(sorted(word))

            if identity not in groups:
                groups[identity] = [] # this itself is a mini-list

            groups.get(identity).append(word)
            # fyu "groups.get(identity)" is the curr []

        return list(groups.values()) # values are the lists 

