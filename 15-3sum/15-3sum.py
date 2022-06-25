class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

# sort the array
# time O (nlogn) + O (n^2)  = O(n^2)
# Space O(n)

        res = []
# sort the array
        nums.sort()
        
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
# 2 pointers
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else: 
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res