class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in range(len(tokens)):
            if tokens[i] == "+":
                val = stack.pop() + stack.pop()
                stack.append(val)
            elif tokens[i] == "*":
                val = stack.pop() * stack.pop()
                stack.append(val)
            elif tokens[i] == "/":
                denominator = stack.pop()
                numerator = stack.pop()
                val = int(float(numerator / denominator))
                stack.append(val)
            elif tokens[i] == "-":
                val2 = stack.pop()
                val1 = stack.pop()
                val = val1 - val2
                stack.append(val)
            else:
                stack.append(int(tokens[i]))
        
        return stack[0]