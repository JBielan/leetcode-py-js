class Solution:
	def bitwiseComplement(self, N: int) -> int:
		binary = list(bin(N)[2:])       # binary representation with deducted 0b at the beginning converted into a list
		for i in range(len(binary)):        # iterate through binary list
			binary[i] = str(abs(int(binary[i]) - 1))        # exchange 0s and 1s and get back to (list of) strings


		return int(''.join(binary), 2)      # return int representation of a binary string (list has been joined)