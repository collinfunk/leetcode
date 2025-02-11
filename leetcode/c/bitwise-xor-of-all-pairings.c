/* Leetcode problem 2425: Bitwise XOR of All Pairings. */

int
xorAllNums (int *nums1, int nums1Size, int *nums2, int nums2Size)
{
  int x = 0;
  for (int i = 0; i < nums1Size; ++i)
    x ^= nums1[i];
  int y = 0;
  for (int i = 0; i < nums2Size; ++i)
    y ^= nums2[i];
  return (nums1Size % 2 * y) ^ (nums2Size % 2 * x);
}
