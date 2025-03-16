
/* Leetcode problem 2373: Largest Local Values in a Matrix. */

class LargestLocalValuesinaMatrix
{
  public int[][]
  largestLocal (int[][] grid)
  {
    int rows = grid.length;
    int columns = grid[0].length;
    int[][] result = new int[rows - 2][columns - 2];
    for (int i = 0; i < rows - 2; ++i)
      for (int j = 0; j < columns - 2; ++j)
        result[i][j] = findLargest (grid, i, j);
    return result;
  }

  private int
  findLargest (int[][] grid, int row, int column)
  {
    int max = grid[row][column];
    for (int i = row; i < row + 3; ++i)
      for (int j = column; j < column + 3; ++j)
        max = Math.max (max, grid[i][j]);
    return max;
  }
}
