/* Leetcode problem 704: Binary Search. */

int
search(int *nums, int numsSize, int target)
{
  int left = 0;
  int right = numsSize - 1;
  while (left <= right)
    {
      int middle = (left + right) / 2;
      if (nums[middle] < target)
        left = middle + 1;
      else if (target < nums[middle])
        right = middle - 1;
      else
        return middle;
    }
  return -1;
}
