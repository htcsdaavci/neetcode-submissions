class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefixes = [0] * n
        suffixes = [0] * n

        prefixes[0] = suffixes[n-1] = 1
        
        for i in range(1, n):
            prefixes[i] = nums[i-1] * prefixes[i-1]
        for i in range(n-2, -1, -1):
            suffixes[i] = nums[i+1] * suffixes[i+1]
        for i in range(n):
            res[i] = prefixes[i] * suffixes[i]
        return res
