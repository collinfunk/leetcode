/* Leetcode problem 405: Convert a Number to Hexadecimal.  */

char *
toHex (int num)
{
  static char buffer[10];
  unsigned int value = num;
  char *p = buffer + sizeof buffer - 1;
  *p = 0;

  if (value < 0)
    {
      do
        {
          int rem = value % 16;
          if (rem < 10)
            *--p = '0' + rem;
          else
            *--p = 'a' + rem % 10;
        }
      while ((value /= 16) != 0);

      *--p = '-';
    }
  else
    {
      do
        {
          int rem = value % 16;
          if (rem < 10)
            *--p = '0' + rem;
          else
            *--p = 'a' + rem % 10;
        }
      while ((value /= 16) != 0);
    }

  return p;
}

int
main (void)
{
  return 0;
}
