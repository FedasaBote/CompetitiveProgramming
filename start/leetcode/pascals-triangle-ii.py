class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            prev = self.getRow(rowIndex - 1)
            return [1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1)] + [1]