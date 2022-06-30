class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
# sliding window
# 2 pointers
        count = {}
        res = 0
        
        l = 0
        for r in range(len(s)):
# store in hash table
            count[s[r]] = 1 + count.get(s[r],0)
# number of replaceable cannot be greather than k 
            while (r - l + 1) - max(count.values()) > k:
# shift left pointer
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
        