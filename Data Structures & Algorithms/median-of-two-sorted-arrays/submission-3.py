class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m = len(nums1)
        n = len(nums2)
        half = (m + n) // 2 
        l, r = 0, m - 1

        while True:
            mid1 = (l + r) // 2
            # because half = (mid1 + 1) + (mid2 + 1)
            # mid1 and mid2 are both indices
            mid2 = half - mid1 - 2

            left1 = nums1[mid1] if mid1 >= 0 else float("-inf")
            right1 = nums1[mid1 + 1] if mid1 + 1 < m else float("inf")

            left2 = nums2[mid2] if mid2 >= 0 else float("-inf")
            right2 = nums2[mid2 + 1] if mid2 + 1 < n else float("inf")

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                r = mid1 - 1
            else:
                l = mid1 + 1