class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights or len(heights) < 2: return 0

        # left most
        left = [0] * len(heights)
        for i in range(1, len(heights), 1):
            left[i] = max(left[i - 1], heights[i - 1])

        right = [0] * len(heights)
        for i in range(len(heights) - 2, 0, -1):
            right[i] = max(right[i + 1], heights[i + 1])

        area = 0
        for i, num in enumerate(heights):
            cur = min(left[i], right[i]) - num
            if cur > 0:
                area = area + cur

        return area