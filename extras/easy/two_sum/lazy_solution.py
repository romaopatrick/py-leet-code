class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        r = []
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue

                if nums[i]+nums[j] == target:
                    return [i, j]
        
        return r