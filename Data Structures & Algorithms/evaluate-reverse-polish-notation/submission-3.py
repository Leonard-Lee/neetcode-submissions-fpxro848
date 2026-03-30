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
        return s in "+-*/"

    def calculate(self, val1, val2, operator) -> int:
        if operator == "+":
            return val1 + val2 
        elif operator == "-":
            return val2 - val1
        elif operator == "*":
            return val1 * val2
        elif operator == "/":
            return int(float(val2) / val1)

        