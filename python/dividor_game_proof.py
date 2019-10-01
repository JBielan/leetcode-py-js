class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0

    '''
    The player who make action on even always win as he can always choose 1 and the second player will not be able to find dividor to leave the second player on odd.
    All dividors of odd numbers are also odd which gives even number after substraction. From odd number it's enough to choose 1 and the situation repeats.
    In the end the "odd" player always make action on 3 and finally lose the game. 
    '''