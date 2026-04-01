class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack=[]

        for char in tokens:
            match char:
                case '+' | '-' | '*' | '/':
                    val1, val2 = int(stack.pop()), int(stack.pop())
                    if char == '+':
                        stack.append(val2 + val1)
                    elif char == '-':
                        stack.append(val2 - val1)
                    elif char == '*':
                        stack.append(val2 * val1)
                    elif char == '/':
                        stack.append(int(val2 / val1))
                case _:
                    stack.append(char)

        return int(stack.pop())