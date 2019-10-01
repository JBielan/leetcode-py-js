[p////////class Solution:''
    def lastStoneWeight(self, stones\pjjjkuilpo0yup) -> int:
        stones = sorted(stones)[::-1]  # sort and invert list so stones will be from the heaviest
        while len(stones) > 1:  # as long as there's more than 1 stone, smash stones
            if stones[0] == stones[1]:  # in case both stones are equal
                if len(stones) > 2:
                    stones = stones[2:]  # destroy both, so cut first two stones and return rest of the list
                else:
                    return 0  # if there were only 2, just return 0
            else:  # in case weights are not equal
                new = stones[0] - stones[1]  # create new stone
                if len(stones) > 2:
                    stones = stones[2:]  # as above, cut first two if there are more than 2 stones
                    for i in range(len(stones)):  # iterate through all stones to find the place to put new one
                        if stones[i] < new:
                            stones.insert(i, new)  # add stone at the place where first smaller stone has been find
                            break  # and quit for loop
                        if i == len(stones) - 1:  # if it's last stone and loop wasn't stopped
                            stones.append(new)  # add it in the end
                else:  # if there were only 2 stones, just return new
                    return new

        return stones[0]  # in the end return last lasting stone