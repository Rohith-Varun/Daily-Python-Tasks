class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        # Initialize the dp array with the bottom row of the triangle
        dp = triangle[-1][:]
        
        # Start from the second to last row and move upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Calculate the minimum path to the current cell
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
                
        # The top element will contain the minimum path sum
        return dp[0]
