class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        
        for i in range(numRows):
            # Start each row with 1s
            row = [1] * (i + 1)
            
            # Fill in the internal values (sum of two numbers directly above)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                
            triangle.append(row)
            
        return triangle
      
