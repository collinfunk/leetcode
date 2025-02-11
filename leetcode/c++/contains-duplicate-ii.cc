
/* Leetcode problem 219: Contains Duplicate II. */

#include <cmath>
#include <unordered_map>
#include <vector>

class Solution
{
public:
  bool
  containsNearbyDuplicate (std::vector<int> &nums, int k)
  {
    std::unordered_map<int, int> table;
    for (int i = 0; i < nums.size (); ++i)
      {
        if (table.count (nums[i]) && abs (i - table[nums[i]]) <= k)
          return true;
        table[nums[i]] = i;
      }
    return false;
  }
};
