// Leetcode problem 3432: Count Partitions with Even Sum Difference.

struct Solution {}

impl Solution {
    pub fn count_partitions(nums: Vec<i32>) -> i32 {
        let mut result = 0;
        let mut left_sum = 0;
        let total_sum: i32 = nums.iter().sum();
        for num in nums[..nums.len() - 1].iter() {
            left_sum += num;
            if (left_sum - (total_sum - left_sum)) % 2 == 0 {
                result += 1
            }
        }
        result
    }
}

fn main() {}
