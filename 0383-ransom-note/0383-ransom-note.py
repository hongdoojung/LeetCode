class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        correct = True
        for s in ransomNote:
            try:
                magazine.remove(s)
            except ValueError:
                correct = False
                break
        return correct
