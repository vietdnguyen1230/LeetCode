class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#     use hashmap
        prevMap = {}
        
        for i, n in enumerate(nums):
#     find difference
            diff = target - n
#     if difference is already in hashmap
            if diff in prevMap:
                return [prevMap[diff], i]
#     otherwise add to hashmap
            else:
                prevMap[n] = i
        
        return