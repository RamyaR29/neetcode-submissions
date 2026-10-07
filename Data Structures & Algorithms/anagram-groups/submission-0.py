class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        result = []
        for str in strs:
            sortedstr = "".join(sorted(str))
            if sortedstr not in hash:
                hash[sortedstr] = []
            hash[sortedstr].append(str)

        for key,val in hash.items():
            result.append(val)

        return result