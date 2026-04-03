class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l, r = 0, len(nums) -1
        # if we need to find exactly the num, we need to use <=
        while l <= r:
            mid = l + (r -l ) // 2

            if target == nums[mid]:
                return mid

            # left sorted part
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # right sorted part
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

        