class Solution:
    def trap(self, height: List[int]) -> int:
        preMax = [0] * len(height)
        curMax = 0
        for i in range(len(height)):
            preMax[i] = curMax
            curMax = max(curMax, height[i])

        curMax = 0
        suffixMax = [0] * len(height)
        for i in range(len(height) - 1, -1, -1):
            suffixMax[i] = curMax
            curMax = max(curMax, height[i])

        res = 0
        for i in range(len(height)):
            minHeight = min(preMax[i], suffixMax[i])
            if minHeight > height[i]:
                res += minHeight - height[i] 

        return res


        