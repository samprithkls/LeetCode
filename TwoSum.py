"""
    1.TwoSum
    -LeetCode
    -Easy

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i]+nums[j]==target):
                    if (nums[i]==nums[j] and i==j):
                        continue
                    else:    
                        return i,j