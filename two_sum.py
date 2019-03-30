class Solution:
    def twoSum(self, nums, target):

        # Numbers that are needed to meet the target will be stored here along with an index of a complementary number.
        wanted_nums = {}

        # Interating through numbers list
        for i in range(len(nums)):

            # If number in wanted_nums it means we've got the sum!
            if nums[i] in wanted_nums:
                return [wanted_nums[nums[i]], i]

            # If not, we store the difference (so the number we seek) along with an index
            else:
                wanted_nums[target - nums[i]] = i

"""
This way the number of iterations is the smallest because all wanted numbers are stored in a memory.

I hope I helped you in some way. If you like this solution, I'll be very happy if you click "Star" on my Github page:
https://github.com/JBielan/leetcode-python

Thank you!
"""