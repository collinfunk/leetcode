/* Leetcode problem 2971: Find Polygon With the Largest Perimeter. */

#include <stdlib.h>

static int compare (const void *ptr1, const void *ptr2);

long long
largestPerimeter (int *nums, int numsSize)
{
  long long side_sum = 0;
  long long result = -1;

  qsort (nums, numsSize, sizeof (int), compare);

  for (int i = 0; i < numsSize; ++i)
    {
      if (nums[i] < side_sum)
        result = nums[i] + side_sum;
      side_sum += nums[i];
    }
  return result;
}

static int
compare (const void *ptr1, const void *ptr2)
{
  const int a = *(const int *) ptr1;
  const int b = *(const int *) ptr2;

  if (a < b)
    return -1;
  else if (a > b)
    return 1;
  else /* a == b */
    return 0;
}
