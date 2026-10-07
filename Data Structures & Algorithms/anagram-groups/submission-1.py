class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        result = []
        for str in strs:
            sortedstr = "".join(sorted(str))
            hash[sortedstr].append(str)

        for key,val in hash.items():
            result.append(val)

        return result