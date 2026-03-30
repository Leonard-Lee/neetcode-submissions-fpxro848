class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1

        # use bucket sort to sort the frequency
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, val in frequency.items():
            bucket[val].append(key)

        ret = []
        size = 0
        for i in range(len(nums), 0, -1):
            if (len(bucket[i]) > 0): 
                ret.extend(bucket[i]) # can a list directly append a list?
                size += len(bucket[i])
                if size >= k: break

        return ret