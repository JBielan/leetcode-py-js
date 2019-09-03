class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        return len(set(nums)) != len(nums)  # set cuts duplicates so len will be smaller if there are any