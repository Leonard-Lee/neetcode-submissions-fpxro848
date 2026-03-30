class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0.0
        elif not nums1:
            size = len(nums2)
            if size % 2:
                return nums2[size // 2]
            else:
                return (nums2[size // 2] + nums2[size // 2 - 1]) / 2
        elif not nums2:
            size = len(nums1)
            if size % 2:
                return nums1[size // 2]
            else:
                return (nums1[size // 2] + nums1[size // 2 - 1]) / 2
             
        A = nums1
        B = nums2
        half = (len(A) + len(B)) // 2

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1
        print (str( (0 - 1) // 2))
        while True:
            m = (r + l) // 2 # index for the smaller one
            big_m = half - m - 2 # index for the bigger array

            Aleft = A[m] if m >=0 else float("-inf")
            Aright = A[m + 1] if m + 1 < len(A) else float("inf")
            Bleft = B[big_m] if big_m >= 0 else float("-inf")
            Bright = B[big_m + 1] if big_m + 1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if (len(A) + len(B)) % 2:
                    return min(Aright, Bright)
                else: # even
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = m - 1
            elif Bleft > Aright:
                l = m + 1

        
        