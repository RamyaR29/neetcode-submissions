class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash = {}
        for ch in s:
            hash[ch] = hash.get(ch,0)+1
        for ch in t:
            if ch in hash and hash[ch] > 0:
                hash[ch] = hash[ch]-1
            else:
                return False
        return True