# Last updated: 4/20/2025, 11:18:24 PM
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """

        jewels = list(jewels)
        stones = list(stones)

        count = 0

        for i in stones:
            if i in jewels:
                count+= 1
        return count
        