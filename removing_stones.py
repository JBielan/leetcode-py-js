class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


"""
Basing on explanation you can assume it's your turn. 

1. When there's 1,2 or 3 stones you just win in the first move.
2. When there is 4 stones, you can do anything and villain will win in next move.
3. When there are 5,6 or 7 stones, you can put villain in a situation with 4 stones, so you always win.
4. When there are 8 stones whatever you do, villain will be anle to put you on 4 stones.
5. When there are 9,10 or 11 stones you can put villain in a situation with 8 stones and so on. 

The only losing situation is when there is number of stones divisible by 4. Other way you just put villain in divisible by 4 situation and you win. 
"""