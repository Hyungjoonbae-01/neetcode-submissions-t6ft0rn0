class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        curr = 0
        for char in tokens:
            print(stack)
            if self.is_integer(char):
                stack.append(int(char))
            elif char == "+":
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(s1+s2)
            elif char == "-":
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(s1-s2)
            elif char == "*":
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(s1*s2)
            elif char == "/":
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(int(float(s1) / s2))
        return stack.pop()
            

    def is_integer(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False
            