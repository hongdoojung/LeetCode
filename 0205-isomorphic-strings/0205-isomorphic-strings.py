class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_hash_map = {}
        t_hash_map = {}
        
        k = 1
        for i in range(len(s)):
            if x:= s_hash_map.get(s[i]):
                if x != t_hash_map.get(t[i]):
                    return False
            else:
                if t_hash_map.get(t[i]):
                    return False
                s_hash_map.update({s[i]: k})
                t_hash_map.update({t[i]: k})
                k += 1
        return True