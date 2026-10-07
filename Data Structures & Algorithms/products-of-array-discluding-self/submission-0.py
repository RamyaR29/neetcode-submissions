class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1] * (len(nums))
        for i,n in enumerate(nums):
            for j in range(len(nums)):
                if j != i:
                    prefix_prod[j] *= n
        
        return prefix_prod