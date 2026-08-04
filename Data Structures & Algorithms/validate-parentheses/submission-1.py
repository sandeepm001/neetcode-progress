class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_bracket = "[{("
        hm = {
            '[':']',
            '{':'}',
            '(':')'
        }
        for ch in s:
            if ch in open_bracket:
                stack.append(ch)
            else:
                if stack and hm[stack[-1]]==ch:
                    stack.pop()
                else:
                    return False
        return len(stack)==0
