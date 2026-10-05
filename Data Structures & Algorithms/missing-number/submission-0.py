class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        slice = all[:len(nums)+1]
        print(slice)
        for num in slice:
            print(num)
            if num not in nums:
                return num
        return 0
            