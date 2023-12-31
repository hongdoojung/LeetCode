class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ("(", "[", "{"):
                stack.append(c)
            else:
                if not stack:
                    return False
                if c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        return False if stack else True
