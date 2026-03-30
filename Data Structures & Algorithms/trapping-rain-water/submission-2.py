class Solution:
    def trap(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        leftMax, rightMax = heights[l], heights[r]

        area = 0
        while l < r:
            if leftMax <= rightMax:
                l += 1
                leftMax = max(leftMax, heights[l])
                area += leftMax - heights[l]
            else:
                r -= 1
                rightMax = max(rightMax, heights[r])
                area += rightMax - heights[r]
        
        return area