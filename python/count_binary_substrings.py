class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            change = 0
            j = i
            while change < 2 and j < len(s) - 1:
                if s[j] != s[j + 1]:
                    change += 1
                    if change == 2:
                        break
                j += 1
                if s[i: j + 1].count('1') == s[i: j + 1].count('0'):
                    count += 1

        return count