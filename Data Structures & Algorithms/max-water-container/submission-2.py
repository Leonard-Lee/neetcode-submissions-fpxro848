class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights or len(heights) < 2: return 0

        l, r = 0, len(heights) - 1
        maxArea = 0
        while l < r:
            maxArea = max(maxArea, min(heights[l], heights[r]) * (r - l))
            if heights[l] <= heights[r]:
                l += 1
            else: 
                r -= 1
        return maxArea

        