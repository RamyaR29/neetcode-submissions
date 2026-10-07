class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum, currsum = nums[0], 0

        for i in range(len(nums)):
            if currsum < 0:
                currsum = 0
            currsum += nums[i]
            maxsum = max(maxsum, currsum)
        return maxsum