class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, val in frequency_map.items():
            buckets[val].append(key)

        resArray = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                resArray.append(num)
                if len(resArray) == k:
                    return resArray
        return resArray

        