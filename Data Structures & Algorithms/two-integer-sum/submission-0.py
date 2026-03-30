class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()

        for idx, num in enumerate(nums):
            if target - num in map:
                return [map.get(target -num), idx] 
            map[num] = idx
        