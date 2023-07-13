class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dict = {}
        reverse_pattern_dict = {}
        split = s.split()
        if len(pattern) != len(split):
            return False
        for i in range(len(pattern)):
            pi = pattern[i]
            word = split[i]
            if not pattern_dict.get(pi):
                if reverse_pattern_dict.get(word):
                    return False
                pattern_dict.update({pi:word})
                reverse_pattern_dict.update({word:pi})
            else:
                if pattern_dict[pi] == word:
                    continue
                else:
                    return False
        return True
