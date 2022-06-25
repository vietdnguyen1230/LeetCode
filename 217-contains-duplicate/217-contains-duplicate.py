class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
#         create hashset 
        hashSet = set()
        
#         iterate through nums
        for n in nums:
#         check if already in hashset
            if n in hashSet:
                return True
#         if not, add to hashset
            else:
                hashSet.add(n)
                
        return False
    
#     Time: O(n) Space: O(n)