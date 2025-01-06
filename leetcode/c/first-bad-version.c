/* Leetcode problem 278: First Bad Version. */

// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int
firstBadVersion (int n)
{
  int left = 0;
  int right = n;
  while (left <= right)
    {
      int middle = left + (right - left) / 2;
      if (isBadVersion (middle))
        right = middle - 1;
      else
        left = middle + 1;
    }
  return left;
}
