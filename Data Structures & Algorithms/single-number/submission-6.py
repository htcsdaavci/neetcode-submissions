class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        is_unique = False
        for num in nums:
            is_unique ^= num            
        
        return is_unique