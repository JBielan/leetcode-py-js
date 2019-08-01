class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        Sorted anagrams have to be identical
        """
        return sorted(s) == sorted(t)