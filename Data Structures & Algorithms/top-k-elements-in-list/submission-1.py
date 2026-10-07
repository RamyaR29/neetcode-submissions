class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for num in nums:
            hash[num] = hash.get(num,0)+1
        sorted_hash = sorted(hash.items(), key = lambda x: x[1], reverse = True)
        ans = [sorted_hash[i][0] for i in range(0,k)]
        return ans