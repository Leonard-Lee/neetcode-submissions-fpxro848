class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        l, r = 0, len(nums) - 1
        # if we're going to find the exact one, use <= here
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            # nums = [1, 1, 3, 1], target = 3
            if nums[l] == nums[mid] == nums[r]:
                r -= 1
                l += 1
                continue

            print(mid)
            print(l)
            print(r)
            if nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return False
                    

        