class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        preOp = "+"
        num = 0
        s = s.replace(" ", "")

        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            if not s[i].isdigit() or i == len(s) - 1:
                if preOp == "+":
                    stack.append(num)
                elif preOp == "-":
                    stack.append(-num)
                elif preOp == "*":
                    stack.append(stack.pop() * num)
                elif preOp == "/":
                    stack.append(int(stack.pop() / num))

                num = 0
                preOp = s[i]

        res = 0
        for num in stack:
            res += num
        return res
        