class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        half = (m + n) // 2 # m = 2, n =2
        # half = 2
        l, r = 0, m - 1 
        # l = 1
        # r = 1

        while True:
            mid1 = l + (r - l) // 2
            # mid1 = 1
            mid2 = half - mid1 - 2
            # mid2 = 0

            # [1,2], [3,4]
            mid1Left = nums1[mid1] if mid1 >= 0 else float("-inf")
            # 2
            mid1Right = nums1[mid1 + 1] if mid1 + 1 < m else float("inf")
            # inf
            mid2Left = nums2[mid2] if mid2 >= 0 else float("-inf")
            # 3 
            mid2Right = nums2[mid2 + 1] if mid2 + 1 < n else float("inf")
            # 4

            if mid1Left <= mid2Right and mid2Left <= mid1Right:
                if (m + n) % 2:
                    return min(mid1Right, mid2Right)
                else:
                    return (max(mid1Left, mid2Left) + min(mid1Right, mid2Right)) / 2
            elif mid1Left > mid2Right:
                r = mid1 - 1
                # r = -1 and l = 0
            else:
                l = mid1 + 1

        
        