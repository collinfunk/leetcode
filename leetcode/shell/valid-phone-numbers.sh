#!/bin/sh

# Leetcode problem 193: Valid Phone Numbers.
LC_ALL=C grep -E '^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$' file.txt
