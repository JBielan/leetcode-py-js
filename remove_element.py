class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        while i < len(nums):    # while is better because it checks nums length after every step (and it decreases)
            if nums[i] == val:
                del nums[i]     # delete the item when it's equal to val
                i -= 1          # crucial point - when you delete an item, you have to decrease 1 to stay at the place
            i += 1              # go to the next position

        return len(nums)

"""
 I hope I helped you in some way. If you like this solution, I'll be very happy if you click "Star" on Github:
https://github.com/JBielan/leetcode-python

May the code be with you!
"""