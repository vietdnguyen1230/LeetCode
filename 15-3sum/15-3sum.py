class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, n in enumerate(nums):
# don't want to reuse same variable twice
            if i > 0 and n == nums[i-1]:
                continue

# 2 pointer
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else: 
                    res.append([n, nums[l], nums[r]])
# update pointer
                    l += 1
# don't reuse same variable
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res