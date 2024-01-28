
/* Leetcode problem 1: Two Sum. */

#include <unordered_map>
#include <vector>

using namespace std;

class Solution
{
public:
  vector<int>
  twoSum (vector<int> &nums, int target)
  {
    unordered_map<int, int> table;
    vector<int>::size_type size = nums.size ();

    for (vector<int>::size_type i = 0; i < size; ++i)
      {
        int need = target - nums[i];
        if (table.count (need))
          return { (int) i, table[need] };
        table[nums[i]] = i;
      }
    return {};
  }
};
