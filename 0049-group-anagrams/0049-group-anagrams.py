class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            group_key = tuple(sorted(string))
            group = groups.get(group_key, [])
            group.append(string)
            groups.update({group_key: group})
        return [x for x in groups.values()]
