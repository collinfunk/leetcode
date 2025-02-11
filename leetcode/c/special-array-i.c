/* Leetcode problem 3151: Special Array I. */

bool
isArraySpecial (int *nums, int numsSize)
{
  for (int i = 1; i < numsSize; ++i)
    if ((nums[i] & 1) == (nums[i - 1] & 1))
      return false;
  return true;
}
