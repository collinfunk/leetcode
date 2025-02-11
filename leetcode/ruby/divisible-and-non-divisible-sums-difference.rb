
# Leetcode problem 2894: Divisible and Non-divisible Sums Difference.

# @param {Integer} n
# @param {Integer} m
# @return {Integer}
def difference_of_sums(n, m)
  return n * (n + 1) / 2 - m * (n / m) * (n / m + 1)
end
