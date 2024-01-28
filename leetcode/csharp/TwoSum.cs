
/* Leetcode problem 1: Two Sum. */

using System.Collections.Generic;

public class TwoSum
{
  public int[]
  TwoSum (int[] nums, int target)
  {
    Dictionary<int, int> table = new Dictionary<int, int> ();

    for (int i = 0; i < nums.Length; ++i)
      {
        int value = nums[i];
        int need = target - value;
        if (table.ContainsKey (need))
          return new int[] {table[need], i};
        table[value] = i;
      }

    return null;
  }
}
