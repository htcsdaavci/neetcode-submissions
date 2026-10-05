class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_count +=  1
        if zero_count > 1: 
            return len(nums) * [0]

        res = [0] * len(nums)
        for i, k in enumerate(nums):
            if zero_count:
                if k:
                    res[i] = 0
                else:
                    res[i] = prod
            else: 
                res[i] = prod // k
        return res
