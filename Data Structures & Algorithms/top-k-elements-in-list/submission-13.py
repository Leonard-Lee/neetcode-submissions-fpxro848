class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        countMap = defaultdict(int)
        for num in nums:
            countMap[num] += 1

        freqList = [[] for i in range(len(nums) + 1)]

        for num, count in countMap.items():
            freqList[count].append(num)

        res = []
        for i in range(len(nums), -1, -1):
            for num in freqList[i]:
                res.append(num)

                if len(res) == k:
                    return res
        return res


        