/* Leetcode problem 2429: Minimize XOR. */

#include <limits.h>

int
minimizeXor (int num1, int num2)
{
  int count1 = __builtin_popcount (num1);
  int count2 = __builtin_popcount (num2);
  int result = num1;
  for (int i = 0; i < sizeof num1 * CHAR_BIT; ++i)
    {
      if (count1 > count2 && ((1 << i) & num1) > 0)
        {
          result ^= 1 << i;
          --count1;
        }
      if (count1 < count2 && ((1 << i) & num1) == 0)
        {
          result ^= 1 << i;
          ++count1;
        }
    }
  return result;
}
