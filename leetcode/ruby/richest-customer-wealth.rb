
# Leetcode problem 1672: Richest Customer Wealth.

# @param {Integer[][]} accounts
# @return {Integer}
def maximum_wealth(accounts)
  result = 0
  for customer in accounts
    current = customer.sum
    if result < current
      result = current
    end
  end
  return result
end
