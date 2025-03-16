
/* Leetcode problem 1: Two Sum. */

import java.util.HashMap;

class TwoSum
{
  public int[]
  twoSum (int[] nums, int target)
  {
    HashMap<Integer, Integer> table = new HashMap<> ();

    for (int i = 0; i < nums.length; ++i)
      {
        int value = nums[i];
        int need = target - value;
        if (table.containsKey (need))
          return new int[] { table.get (need), i };
        table.put (value, i);
      }

    return null;
  }
}
