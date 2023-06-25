class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]
        for target in strs[1:]:
            for i, s in enumerate(longest):
                if not target[i:]:
                    longest = longest[:i]
                    break
                elif s != target[i]:
                    longest = longest[:i]
                    break
        return longest