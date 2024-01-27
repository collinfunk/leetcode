/*-
 * Copyright (c) 2023, Collin Funk
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE AUTHORS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */

/* Leetcode problem 14: Longest Common Prefix. */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static char *longestCommonPrefix (char **strs, int strsSize);

int
main (void)
{
  return 0;
}

static char *
longestCommonPrefix (char **strs, int strsSize)
{
  int i = 0;
  size_t prefix_len = 0;
  char *ptr;

  /* Input constraints. */
  if (strsSize < 1 || strsSize > 200)
    abort ();

  /* Base case. */
  if (strsSize == 1)
    return strs[0];

  do
    {
      int j = 0;
      size_t count = 0;
      while (strs[i][j] == strs[i + 1][j])
        {
          count++;
          if (strs[i][j] == '\0')
            break;
          else
            j++;
        }
      if (count == 0)
        return "";
      if (prefix_len == 0 || prefix_len > count)
        prefix_len = count;
      printf ("%zu\n", prefix_len);
    }
  while (++i < strsSize - 1);

  if (prefix_len == 0)
    abort ();

  ptr = malloc (prefix_len + 1);
  memcpy (ptr, strs[0], prefix_len);
  ptr[prefix_len] = '\0';

  return ptr;
}
