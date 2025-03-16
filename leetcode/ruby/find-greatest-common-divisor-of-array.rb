
# Leetcode problem 1979: Find Greatest Common Divisor of Array.

# @param {Integer[]} nums
# @return {Integer}
def find_gcd(nums)
  nums.minmax.reduce(:gcd)
end
