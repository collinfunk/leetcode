
# Leetcode problem 2119: A Number After a Double Reversal.

# @param {Integer} num
# @return {Boolean}
def is_same_after_reversals(num)
  if num == 0 or num % 10 != 0
    return true
  end
  return false
end
