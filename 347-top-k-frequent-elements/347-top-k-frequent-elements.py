class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#  initialize array to hold k occurence
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

#  add to count/ counting the values each time nums appear
        for n in nums:
            count[n] = 1 + count.get(n, 0)
#  going through each of items we counted/ this value n occurs c number of times
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
# starting from highest freqeuncy
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        # O(n)
        
        
        
        
