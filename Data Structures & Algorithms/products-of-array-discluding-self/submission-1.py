class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prefix.append(1)
        prev = 1
        for i in range(1, len(nums)):
            num = prev*nums[i-1]
            prefix.append(num)
            prev = num

        prev = 1
        suffix = [1] * len(nums)
        for i in range(len(nums)-2, -1,-1):
            num = prev*nums[i+1]
            suffix[i] = num
            prev = num

        ans = [1] * len(nums)
        for i in range(0, len(nums)):
            ans[i] = prefix[i]*suffix[i]
        return ans



        