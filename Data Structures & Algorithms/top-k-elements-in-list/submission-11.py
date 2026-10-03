from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n+1)]
        once = []

        for num, freq in counts.items():
            if freq == 1:
                once.append(num)
            buckets[freq].append(num)
        
        frequencies = []
        for i in range(len(buckets)-1,1,-1):
            for num in buckets[i]:
                frequencies.append(num)
                if len(frequencies) == k:
                    return frequencies
        for num in once:
            if len(frequencies) < k:
                frequencies.append(num)
            else:
                break

        return frequencies