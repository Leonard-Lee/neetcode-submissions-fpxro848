class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # key: num / val: frequency
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)] 
        for key, val in count.items():
            buckets[val].append(key)

        ret = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                ret.append(num)
                if len(ret) == k: return ret

        return ret


        