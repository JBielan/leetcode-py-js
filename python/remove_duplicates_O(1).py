class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_idx = 0

        while curr_idx < len(
                nums) - 1:  # iterating through nums list till next-to-last element (curr_idx + 1 always checked)
            if nums[curr_idx] == nums[curr_idx + 1]:  # if current and next element are the same
                del nums[curr_idx]  # current element is deleted
                curr_idx -= 1  # to stay at the same place in list, we have to dicrease 1 (1 will be added in the next step)
            curr_idx += 1  # going further in the list

        return len(nums)

    # what's important here is the fact, that in while loop condition is checked with every step,
    # so len(nums) when del is decreasing and will not cause index error in the end of iteration
    # as in for loop

"""
I hope I helped you in some way. If you like this solution, I'll be very happy if you click "Star" on Github:
https://github.com/JBielan/leetcode-python

May the code be with you!
"""