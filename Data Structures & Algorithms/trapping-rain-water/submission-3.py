class Solution:
    def trap(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        leftMax, rightMax = heights[l], heights[r]

        area = 0
        while l < r:
            if leftMax <= rightMax:
                # water cannot be trapped in the very first bar
                l += 1
                # to avoid negtive number
                # if leftMax <= heights[l] => return negative and zero
                # => it is updated to heights[l] => return zero only 
                # if leftMax > heights[l] => always return postive for area
                # that means leftMax will NOT be updated to heights[l]
                leftMax = max(leftMax, heights[l])
                area += leftMax - heights[l]
            else:
                # water cannot be trapped in the very last bar
                r -= 1
                rightMax = max(rightMax, heights[r])
                area += rightMax - heights[r]
        
        return area