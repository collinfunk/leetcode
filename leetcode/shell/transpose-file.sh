#!/bin/sh

# Leetcode problem 194: Transpose File.
LC_ALL=C awk '
  {
    for (i = 1; i <= NF; ++i) {
      if (NR == 1) {
        table[i] = $i;
      } else {
        table[i] = table[i] " " s$i;
      }
    }
  }
END {
  for (i = 1; i <= NF; ++i) {
    print table[i];
  }
}' file.txt
