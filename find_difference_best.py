class Solution(object):
    def findTheDifference(self, s, t):
        """
        Get every letter from bigger string (without repetition - by set(t) ) and check whether every letter
        has the same count for s and t. It's not my solution but it's brilliant enough to explain and share!
        This smart move together with list comprehension gives trully lightening speed.
        """
        return ''.join(c for c in set(t) if s.count(c) != t.count(c))