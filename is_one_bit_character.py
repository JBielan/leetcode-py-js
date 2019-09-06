class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        """
        The idea is to deduct (1, 1) or (1, 0) or (0) as long as 2 characters remain.
        If those characters are (1, 1) or (1, 0) it's not possible, otherwise it's possible.
        We have to assume decoding bits is possible as there aren't instructions.
        """
        if bits[-1] != 0:
            return False
        elif bits[-2:] != [1, 0]:
            return True

        while len(bits) > 2:
            if bits[0] == 0:
                bits = bits[1:]
            elif bits[:2] == [1, 0] or bits[:2] == [1, 1]:
                bits = bits[2:]

        if bits == [1, 1] or bits == [1, 0]:
            return False
        else:
            return True
