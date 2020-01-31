class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, best = 0, len(height) - 1, 0  # set left/right side and best

        while l != r:       # as long as sides don't touch each other
            area = min(height[l], height[r]) * (r - l)      # calculate area
            if area > best: best = area     # set it to best if it's bigger
            if height[l] < height[r]:       # if left bar is smaller
                l += 1      # move left one to the right
            else:
                r -= 1      # otherwise move right one to the lef
        return best     # in the end return the best result