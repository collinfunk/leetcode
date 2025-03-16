
/* Leetcode problem 1827: Minimum Operations to Make the Array Increasing. */

class MinimumOperationstoMaketheArrayIncreasing
{
  public int
  minOperations (int[] nums)
  {
    int operations = 0;
    for (int i = 1; i < nums.length; ++i)
      {
        if (nums[i] == nums[i - 1])
          {
            operations++;
            nums[i]++;
          }
        else if (nums[i] < nums[i - 1])
          {
            int need = (nums[i - 1] - nums[i]) + 1;
            operations += need;
            nums[i] += need;
          }
      }
    return operations;
  }
}
