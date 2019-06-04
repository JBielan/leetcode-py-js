class Solution(object):
    def singleNumber(self, nums):
        return sum(list(set(nums)))*2 - sum(nums)