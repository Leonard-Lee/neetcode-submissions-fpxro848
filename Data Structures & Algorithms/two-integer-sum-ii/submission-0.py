class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers or len(numbers) == 1: return []

        check_dict = {}
        for i, num in enumerate(numbers):
            if target - num in check_dict:
                return[check_dict[target - num] + 1, i + 1]
            else:
                check_dict[num] = i 
        return []
        