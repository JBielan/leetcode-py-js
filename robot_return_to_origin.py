class Solution:
	def judgeCircle(self, moves: str) -> bool:
		return (moves.count('D') == moves.count('U') and moves.count('L') == moves.count('R'))