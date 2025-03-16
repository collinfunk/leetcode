// Leetcode problem 1749: Maximum Absolute Sum of Any Subarray.

struct Solution {}

impl Solution {
    pub fn max_absolute_sum(nums: Vec<i32>) -> i32 {
        let mut current_positive_sum = 0;
        let mut current_negative_sum = 0;
        let mut maximum_absolute_sum = 0;
        for num in nums {
            current_positive_sum = (current_positive_sum + num).max(0);
            current_negative_sum = (current_negative_sum - num).max(0);
            maximum_absolute_sum = maximum_absolute_sum
                .max(current_positive_sum)
                .max(current_negative_sum);
        }
        maximum_absolute_sum
    }
}

fn main() {}
