class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # bucket sort; we need n buckets and n is len(nums) + 1
        bucket = [[] for _ in range(len(nums) + 1)] 
        for key, val in freq.items():
            bucket[val].append(key)

        ret = []
        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                ret.append(num)
                if len(ret) == k: return ret
    
        return ret


        