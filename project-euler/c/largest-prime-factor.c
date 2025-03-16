
#include <stdio.h>
#include <stdbool.h>

static bool
is_prime (int value)
{
  if (value <= 1)
    return false;
  if (value == 2 || value == 3)
    return true;
  int divisor = 3;
  int square = divisor * divisor;

  while (square < value && (value % divisor))
    {
      divisor++;
      square += 4 * divisor;
      divisor++;
    }

  return value % divisor != 0;
}

int
main (void)
{
  int result = 0;
  for (int i = 3; i <= 600851475143 / 3; i += 2)
    {
      if (600851475143 % i == 0)
        {
          int value = 600851475143 / i;
          if (is_prime (value))
            {
              result = value;
              break;
            }
        }
    }
  printf ("%d\n", result);
  return 0;
}
