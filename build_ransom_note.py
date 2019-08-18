class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		i = 0       # index for iterating ransom note
		while i < len(ransomNote):      # for all ransomNote items
			if ransomNote[i] not in magazine:
				return False        # put it at the beginning for faster execution
			magazine = magazine.replace(ransomNote[i], "", 1)       # remove first appearance in magazine of a letter from ransom note
			i += 1      # go to the next letter
		return True     # when out of while loop it means  there's enough letters in a magazine