
# Leetcode problem 1051: Height Checker.

# @param {Integer[]} heights
# @return {Integer}
def height_checker(heights)
  sorted_heights = heights.sort
  result = 0
  for i in 0..heights.size
    if heights[i] != sorted_heights[i]
      result += 1
    end
  end
  return result
end
