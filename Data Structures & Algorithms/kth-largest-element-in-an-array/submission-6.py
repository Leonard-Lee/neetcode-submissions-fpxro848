import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            randIdx = random.randint(l, r)
            nums[r], nums[randIdx] = nums[randIdx], nums[r]

            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    # swap
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[r], nums[p] = nums[p], nums[r]

            if p < k:
                return quickSelect(p + 1, r)
            elif p > k:
                return quickSelect(l, p - 1)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)
        