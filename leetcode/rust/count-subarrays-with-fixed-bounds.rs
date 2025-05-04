// Leetcode problem 2444: Count Subarrays With Fixed Bounds.

struct Solution {}

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, min_k: i32, max_k: i32) -> i64 {
        let mut result = 0;
        let mut invalid_index = -1_i64;
        let mut max_index = -1_i64;
        let mut min_index = -1_i64;
        for (i, &num) in nums.iter().enumerate() {
            if num == min_k {
                min_index = i as i64;
            }
            if num == max_k {
                max_index = i as i64;
            }
            if num < min_k || num > max_k {
                invalid_index = i as i64;
            }
            result += (min_index.min(max_index) - invalid_index).max(0);
        }
        result
    }
}

fn main() {}
