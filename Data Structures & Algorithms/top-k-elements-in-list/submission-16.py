class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = defaultdict(int)
        for num in nums:
            countMap[num] += 1

        buckets = [[] for i in range(len(nums) + 1)]
        for num, count in countMap.items():
            buckets[count].append(num)

        res = []
        for i in range(len(nums), -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res


        