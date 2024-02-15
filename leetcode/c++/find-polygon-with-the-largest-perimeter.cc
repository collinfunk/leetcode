/* Leetcode problem 2971: Find Polygon With the Largest Perimeter. */

#include <algorithm>
#include <vector>

class Solution
{
public:
  long long
  largestPerimeter (std::vector<int> &nums)
  {
    long long side_sum = 0;
    long long result = -1;

    std::sort (nums.begin (), nums.end ());

    for (std::vector<int>::size_type i = 0; i < nums.size (); ++i)
      {
        if (nums[i] < side_sum)
          result = nums[i] + side_sum;
        side_sum += nums[i];
      }
    return result;
  }
};
