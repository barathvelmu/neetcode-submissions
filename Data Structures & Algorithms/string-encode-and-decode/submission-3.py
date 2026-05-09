class Solution:

    def encode(self, strs: List[str]) -> str:
        # the goal is to encode w: length + # + string 
        encoded = ""
        for word in strs: 
            encoded += str(len(word)) + "#" + word
        
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s): # at first, this is a number 
            j = i 
            
            while s[j] != "#": 
                j = j + 1
            
            length = int(s[i:j]) # this will be up to "j" (non inclusive of j), so only num
            word_start_index = j+1
            word_end_index = word_start_index + length 

            word = s[word_start_index:word_end_index] # word_end_index always 1 over

            strs.append(word)

            i = word_end_index
        
        return strs



                

                


