
/* Leetcode problem 3438: Find Valid Pair of Adjacent Digits in String. */

#include <string>

#include <string>

class Solution {
public:
  std::string
  findValidPair (std::string s)
  {
    char counts[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
    for (char c : s)
      counts[c - '1']++;
    for (std::size_t i = 0; i < s.length() - 1; ++i)
      {
        if (s[i] != s[i + 1] && counts[s[i] - '1'] == s[i] - '0'
            && counts[s[i + 1] - '1'] == s[i + 1] - '0')
          {
            std::string result;
            result.push_back(s[i]);
            result.push_back(s[i + 1]);
            return result;
          }
      }
    return std::string();
  }
};
