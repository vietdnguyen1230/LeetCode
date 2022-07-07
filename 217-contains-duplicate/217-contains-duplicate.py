class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        
        for n in nums:
            if n in duplicate:
                return True
            else:
                duplicate.add(n)
        
        return False