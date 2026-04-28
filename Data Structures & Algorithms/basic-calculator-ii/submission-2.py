class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        s = s.replace(" ", "")
        op = "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            if not s[i].isdigit() or i == len(s) - 1:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop() * num)
                elif op == "/":
                    stack.append(int(stack.pop() / num))

                op = s[i]
                num = 0
        res = 0
        for num in stack:
            res += num

        return res
        