class Solution:
    def searchInsert(self, nums, target):
        left, right = 0,len(nums)-1     # At the beginning whole range is taken into account (0, len-1)
        while left<right:               # As long as bottom frontier touches upper, constantly narrow range
            mid = (left+right)//2       # Always check the middle of the range
            if nums[mid]<target:        # If middle is smaller, you cut bottom by setting bottom to middle
                left = mid+1            # Left forntier is set to the middle
            else:
                right = mid             # If it's bigger or equal, cut upper half by setting upper to middle

        # Outer while, which means bottom frontier touched upper (index has been found)

        if nums[left]<target:           # It means algorithm touched the end of the list, so add target as last item
            return left+1
        return left                     # Otherwise index is the bottom frontier

"""
I hope I helped you in some way. If you like this solution, I'll be very happy if you click "Star" on Github:
https://github.com/JBielan/leetcode-python

As well feel free to follow my account for daily coding solutions and machine-learning/data-science projects:
https://github.com/JBielan

May the code be with you!
"""
