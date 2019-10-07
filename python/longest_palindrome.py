class Solution(object):
    def longestPalindrome(self, s):
        """
        type s: str
        rtype: str
        """
        longest = ""
        i = 0
        # here i represent the center position of the string
        while i < len(s):
            l = i
            r = i
            # find the duplicated string
            while (r < len(s) - 1 and s[r] == s[r + 1]):
                r = r + 1
            # jump to the right side of the duplicated string in next iteration
            i = r + 1
            ans = find_longest(s, l, r)
            if len(longest) < len(ans):
                longest = ans
        return longest


def find_longest(s, l, r):
    while (l >= 0 and r < len(s) and s[l] == s[r]):
        l = l - 1
        r = r + 1
    return s[l + 1:r]