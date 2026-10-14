class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for symbol in s:
            if symbol in '([{':
                stack.append(symbol)
            elif (symbol == ')') and (len(stack) != 0) and (stack[-1] == '('):
                stack.pop()
            elif (symbol == ']') and (len(stack) != 0) and (stack[-1] == '['):
                stack.pop()
            elif (symbol == '}') and (len(stack) != 0) and (stack[-1] == '{'):
                stack.pop()
            else:
                return False
        return len(stack) == 0
