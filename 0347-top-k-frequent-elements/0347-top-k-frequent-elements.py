class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k==len(nums):
            return nums
        
        c=Counter(nums)
        return nlargest(k,c.keys(),c.get)
        