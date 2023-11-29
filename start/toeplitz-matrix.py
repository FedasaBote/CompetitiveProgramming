class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        i=0
        while i< len(matrix[0]):
            row,col = 0,i
            first = matrix[row][col]
            while row<len(matrix) and col<len(matrix[0]):
                if matrix[row][col]!=first:
                    return False
                row+=1
                col+=1
            i+=1
        j=0
        while j< len(matrix):
            row,col = j,0
            first = matrix[row][col]
            while row<len(matrix) and col<len(matrix[0]):
                if matrix[row][col]!=first:
                    return False
                row+=1
                col+=1
            j+=1

        return True
        