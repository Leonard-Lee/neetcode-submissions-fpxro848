class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        
        ret = defaultdict(list)
        for key, val in frequency_map.items():
            ret[val].append(key)

        resArray = []
        for i in range(len(nums), 0, -1):
            print("i: " + str(i))
            print("ret[i]: " + str(ret[i]))
            for num in ret[i]:
                resArray.append(num)
                if len(resArray) == k:
                    return resArray
        return resArray

        