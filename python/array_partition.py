class Solution:
    def arrayPairSum(self, nums):
        nums = sorted(nums)  # to make it as big as possible, array should be sorted
        result = 0  # sum will be stored here
        for i in range(0, len(nums) - 1, 2):  # iterate from first to second last counting every second element
            result += min(nums[i], nums[i + 1])  # get min and add to the result

        return result

"""
I hope I helped you in some way. If you like this solution, I'll be very happy if you click "Star" on Github:
https://github.com/JBielan/leetcode-python

As well feel free to follow my account for daily coding solutions and machine-learning/data-science projects:
https://github.com/JBielan

May the code be with you!

"""