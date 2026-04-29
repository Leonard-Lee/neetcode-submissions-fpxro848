import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1

        k = len(nums) - k

        def quickSelect(l, r):
            randIdx = random.randint(l, r)
            nums[r], nums[randIdx] = nums[randIdx], nums[r]
            
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[r], nums[p] = nums[p], nums[r]

            if k < p:
                return quickSelect(l, p - 1)
            elif k > p:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)
        