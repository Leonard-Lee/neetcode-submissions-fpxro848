class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]":
                substr_list = []
                while stack and stack[-1] != "[":
                    substr_list.append(stack.pop())
                stack.pop()
                substr_list.reverse()
                substr = "".join(substr_list)

                num_list = []
                while stack and stack[-1].isdigit():
                    num_list.append(stack.pop())

                num_list.reverse()
                num = "".join(num_list)
                stack.append(int(num) * substr)
            else:
                stack.append(c)

        return "".join(stack)

        