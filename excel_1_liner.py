class Solution:
    def titleToNumber(self, s: str) -> int:
        """
        Let's start from the inside of formula:
        1. ord(c)-64 gives values for chars A-1 to Z-26
        2. value*26**i gives the result for digit because string is reversed s[::-1]
        3. i is index and c is char
        4. in the end it's enough to sum all digits (from last to first)
        """
    	return sum([(ord(c)-64)*26**i for i,c in enumerate(s[::-1])])