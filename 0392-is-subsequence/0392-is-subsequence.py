class Solution:
    def isSubsequence(self, t: str, s: str) -> bool:
        t_i = 0
        for i in range(len(s)):
            if t_i == len(t):
                break
            if s[i] == t[t_i]:
                t_i += 1
        if t_i == len(t):
            return True
        else:
            return False
                