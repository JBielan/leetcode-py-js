class Solution:
	def letterCasePermutation(self, S: str) -> List[str]:
		'''
		Easy algorithm:
		If char is a number, add it to every word in results.
		If char is alphabetic, duplicate every word with upper char in the end.
		Add lower char to the first half of words (those which upper wasn't added).
		'''
		if S[0].isalpha():
			results = [S[0].lower(), S[0].upper()]
		else:
			results = [S[0]]

		for i in range(1, len(S)):
			if S[i].isalpha():
				res_temp = results.copy()
				for word in results:
					res_temp.append(word + S[i].upper())

				for j in range(int(len(res_temp) / 2)):
					res_temp[j] += S[i].lower()

				results = res_temp.copy()

			else:
				for k in range(len(results)):
					results[k] += S[i]


		return results