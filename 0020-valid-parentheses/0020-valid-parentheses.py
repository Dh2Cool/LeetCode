class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if len(stack) != 0:
                    if (ch == ')' and stack[-1] == '(') or (ch == '}' and stack[-1] == '{') or (ch == ']' and stack[-1] == '['):
                        stack.pop(-1)
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        