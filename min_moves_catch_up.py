class Solution:
    def minMoves(self, nums: List[int]) -> int:
        cnt = 0
        while len(set(nums)) != 1:
            nums.sort()
            diff = nums[-1] - nums[0]
            for i in range(len(nums) - 1):
                nums[i] += diff
            cnt += diff

        return cnt