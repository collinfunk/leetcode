
/* Leetcode problem 1678: Goal Parser Interpretation. */

class GoalParserInterpretation
{
  public String
  interpret (String command)
  {
    int i = 0;
    StringBuilder result = new StringBuilder ();
    while (i < command.length ())
      {
        if (command.charAt (i) == 'G')
          {
            result.append ("G");
            i += 1;
          }
        else /* command.charAt (i) == '(' */
          {
            if (command.charAt (i + 1) == ')')
              {
                result.append ("o");
                i += 2;
              }
            else
              {
                result.append ("al");
                i += 4;
              }
          }
      }
    return result.toString ();
  }
}
