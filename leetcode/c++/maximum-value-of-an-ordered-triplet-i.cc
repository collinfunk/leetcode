
/* Leetcode problem 2873: Maximum Value of an Ordered Triplet I. */

#include <algorithm>
#include <vector>

class Solution
{
public:
  long long int
  maximumTripletValue (std::vector<int> &nums)
  {
    long long int result = 0;
    for (std::vector<int>::size_type i = 0; i < nums.size (); ++i)
      for (std::vector<int>::size_type j = i + 1; j < nums.size (); ++j)
        for (std::vector<int>::size_type k = j + 1; k < nums.size (); ++k)
          {
            long long int current = (nums[i] - nums[j]);
            current *= nums[k];
            result = std::max (result, current);
          }
    return result;
  }
};
