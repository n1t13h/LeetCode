class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = {"+", "-", "*", "/"}
        
        for n in tokens:
            if n not in operators:
                stack.append(int(n))
            else:
                left = stack.pop()
                right = stack.pop()
                
                if n == "+":
                    stack.append(right + left)
                elif n == "-":
                    stack.append(right - left)
                elif n == "*":
                    stack.append(right * left)
                else:
                    stack.append(int(right / left))
        
        return stack[0]
