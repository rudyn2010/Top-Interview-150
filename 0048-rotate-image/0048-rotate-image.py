class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                
                #Save the top left
                topLeft = matrix[top][l + i]
                
                #Move bottom left into top left
                matrix[top][l + i] = matrix[bottom  - i][l]
                
                #Move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                #Move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                
                #Move top left into top right
                matrix[top + i][r] = topLeft
                
            r -= 1
            l += 1