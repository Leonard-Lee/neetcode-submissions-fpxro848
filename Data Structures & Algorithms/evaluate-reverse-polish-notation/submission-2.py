class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.isOperator(token):
                stack.append(self.calculate(stack.pop(), stack.pop(), token))
            else:
                stack.append(int(token))
        return stack.pop()


    def isOperator(self, s: str):
        return s == "+" or s == "-" or s == "*" or s == "/" 

    def calculate(self, val1, val2, operator) -> int:
        if operator == "+":
            return int(val2) + int(val1)
        elif operator == "-":
            return int(val2) - int(val1)
        elif operator == "*":
            return int(val2) * int(val1)
        elif operator == "/":
            print(int(val2) // int(val1))
            return int(int(val2) / int(val1))

        