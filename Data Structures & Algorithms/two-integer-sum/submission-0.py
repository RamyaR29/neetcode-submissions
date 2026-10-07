class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        result = []
        i = 0
        for n in nums:
            if target-n in hash:
                result.append(hash[target-n])
                result.append(i)
                return result
            hash[n] = i
            i = i+1
        return result
