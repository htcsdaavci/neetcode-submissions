class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copy = []
        for i, num in enumerate(nums):
            copy.append([num,i])
        copy.sort()
        i, j = 0, len(nums)-1
        while i < j:
            curr = copy[i][0] + copy[j][0]
            if curr == target:
                return [min(copy[i][1], copy[j][1]), max(copy[i][1], copy[j][1])]
            elif curr < target:
                i += 1
            else:
                j -= 1
        return [] 

        