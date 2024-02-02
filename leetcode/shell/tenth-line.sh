#!/bin/sh

# Leetcode problem 195: Tenth Line.

# 1. Sed
sed -n -e '10,10p' file.txt

# 2. Awk
awk 'NR == 10' file.txt

# 3. Awk
awk 'FNR == 10 { print }' file.txt
