class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for each in strs:
            sortedWord = "".join(sorted(each))
            if sortedWord not in hash:
                hash[sortedWord] = []
            hash[sortedWord].append(each)
        ans = []
        for each in hash:
            ans.append(hash[each])
        return ans