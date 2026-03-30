class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_list = []
        for i, num in enumerate(nums):
            new_list.append([num, i])

        new_list.sort()

        i, j = 0, len(new_list) - 1
        while (i < j):
            sum = new_list[i][0] + new_list[j][0] 
            if ( sum == target): 
                return [min(new_list[i][1], new_list[j][1]), max(new_list[i][1], new_list[j][1])]
            elif sum < target:
                i += 1
            else:   
                j -= 1
        return []

        