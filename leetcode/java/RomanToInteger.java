
/* Leetcode problem 13: Roman to Integer. */

class RomanToInteger
{
  public int
  romanToInt (String s)
  {
    int result = 0;
    int i = 0;

    while (i < s.length ())
      {
        if (s.charAt (i) == 'I')
          {
            if (i + 1 >= s.length ())
              {
                result += 1;
                i += 1;
              }
            else if (s.charAt (i + 1) == 'V')
              {
                result += 4;
                i += 2;
              }
            else if (s.charAt (i + 1) == 'X')
              {
                result += 9;
                i += 2;
              }
            else
              {
                result += 1;
                i += 1;
              }
          }
        else if (s.charAt (i) == 'X')
          {
            if (i + 1 >= s.length ())
              {
                result += 10;
                i += 1;
              }
            else if (s.charAt (i + 1) == 'L')
              {
                result += 40;
                i += 2;
              }
            else if (s.charAt (i + 1) == 'C')
              {
                result += 90;
                i += 2;
              }
            else
              {
                result += 10;
                i += 1;
              }
          }
        else if (s.charAt (i) == 'C')
          {
            if (i + 1 >= s.length ())
              {
                result += 100;
                i += 1;
              }
            else if (s.charAt (i + 1) == 'D')
              {
                result += 400;
                i += 2;
              }
            else if (s.charAt (i + 1) == 'M')
              {
                result += 900;
                i += 2;
              }
            else
              {
                result += 100;
                i += 1;
              }
          }
        else if (s.charAt (i) == 'V')
          {
            result += 5;
            i += 1;
          }
        else if (s.charAt (i) == 'L')
          {
            result += 50;
            i += 1;
          }
        else if (s.charAt (i) == 'D')
          {
            result += 500;
            i += 1;
          }
        else if (s.charAt (i) == 'M')
          {
            result += 1000;
            i += 1;
          }
      }

    return result;
  }
}
