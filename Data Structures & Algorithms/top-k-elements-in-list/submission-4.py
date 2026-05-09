class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        # {number: count}

        for num in nums: 
            store[num] = store.get(num, 0) + 1

        # reverse the dictionary 
        sorted_store = sorted(store.items(), key = lambda x: x[1], reverse = True)
        # reverse = True is descending order 

        # sorted() gives you a list now. A list of tuples. 

        blist = []
        for key, value in sorted_store: # sorted_store = list of tuples
            blist.append(key)

        return blist[:k]

        