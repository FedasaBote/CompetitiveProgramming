class Solution:
    def numSubmatrixSumTarget(self,matrix, target):
        rows, cols = len(matrix), len(matrix[0])
        count = 0

        for row in matrix:
            for j in range(1, cols):
                row[j] += row[j - 1]

        for start_col in range(cols):
            for end_col in range(start_col, cols):
                counter = Counter()
                counter[0] = 1
                current_sum = 0

                for row in range(rows):
                    current_sum += matrix[row][end_col] - (matrix[row][start_col - 1] if start_col > 0 else 0)
                    
                    count += counter[current_sum - target]
                    
                    counter[current_sum] += 1

        return count
