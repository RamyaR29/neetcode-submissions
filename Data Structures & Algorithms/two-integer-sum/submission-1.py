class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        ans = []
        for ind,num in enumerate(nums):
            if target-num in hash:
                ans.append(hash[target-num])
                ans.append(ind)
                return ans
            hash[num] = ind
        return null