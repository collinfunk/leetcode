
/* Leetcode problem 2103: Rings and Rods. */

class RingsandRods
{
  public int
  countPoints (String rings)
  {
    int[] array = new int[10];
    for (int i = 0; i < rings.length (); i += 2)
      {
        int bit = 0;
        switch (rings.charAt (i))
          {
          case 'R':
            bit = 0x01;
            break;
          case 'G':
            bit = 0x02;
            break;
          case 'B':
            bit = 0x04;
            break;
          }
        int index = rings.charAt (i + 1) - '0';
        array[index] |= bit;
      }
    int result = 0;
    for (int element : array)
      result += element == 0x07 ? 1 : 0;
    return result;
  }
}
