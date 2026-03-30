class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedPosition = []
        for i in range(len(position)):
            sortedPosition.append((position[i], speed[i]))
        sortedPosition.sort(reverse = True)
        stack = []
        for item in sortedPosition:
            p, s = item
            time = (target - p) / s
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack) 