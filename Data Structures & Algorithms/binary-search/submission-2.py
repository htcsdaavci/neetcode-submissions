class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #if target not in nums:
        #    return -1
        nums.sort()
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + (end - start) // 2)
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                return mid
            
        return -1