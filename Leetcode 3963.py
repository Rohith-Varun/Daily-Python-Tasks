class Solution:
  def createGrid(self, m: int, n: int) -> list[str]:
    grid = []
    for i in range(m):
      row = []
      for j in range(n):
        # Allow free cells on the top row (j == n - 1) or the last column (i == 0)
        if i == 0 or j == n - 1:
          row.append('.')
        else:
          row.append('#')
      grid.append(''.join(row))
    return grid
