/* Leetcode problem 2683: Neighboring Bitwise XOR. */

#include <stdbool.h>

bool
doesValidArrayExist (int *derived, int derivedSize)
{
  int result = 0;
  for (int i = 0; i < derivedSize; ++i)
    result ^= derived[i];
  return result == 0;
}

