class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        globalMax = float("-inf")
        globalMin = float("inf")

        maxVal = 1
        minVal = 1

        for num in nums:
            preMax = maxVal
            maxVal = max(num * maxVal, num * minVal, num)
            minVal = min(num * preMax, num * minVal, num)
            # print("(" + str(maxVal) + ", " + str(minVal) + ")")

            globalMax = max(globalMax, maxVal)
            globalMin = min(globalMin, minVal)
            # print("(" + str(globalMax) + ", " + str(globalMin) + ")")
    
        return globalMax