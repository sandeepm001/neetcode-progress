class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            ch = tokens[i]
            if ch.lstrip('-').isdigit():
                stack.append(int(ch))
            else:
                if ch in '+-*/':
                    if len(stack)>1:
                        n2 = stack.pop()
                        n1 = stack.pop()
                    if ch=='+':
                        stack.append(n1+n2)
                    elif ch=='-':
                        stack.append(n1-n2)
                    elif ch=='*':
                        stack.append(n1*n2)
                    else:
                        stack.append(int(n1/n2))
        return stack[0]