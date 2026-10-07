class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        print(nums)
        # hashset in python = set
        hashset = set(nums)
        best_cnt = 0
        for num in hashset:
            if num-1 not in hashset:
                curr_num = num
                curr_cnt = 1

                while (curr_num+1) in hashset:
                    curr_num += 1
                    curr_cnt += 1
                best_cnt = max(best_cnt, curr_cnt)

        return best_cnt
