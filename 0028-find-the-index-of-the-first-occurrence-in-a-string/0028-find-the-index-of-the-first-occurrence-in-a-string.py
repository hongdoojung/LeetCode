class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        exist = False
        for i, s in enumerate(haystack):
            if s == needle[0]:
                if haystack[i:i+length] == needle:
                    exist = True
                    break
        return i if exist else -1
                