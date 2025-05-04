// Leetcode problem 2962: Count Subarrays Where Max Element Appears at Least K Times.

struct Solution {}

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let max_num = nums.iter().max().unwrap();
        let mut max_indexes = Vec::with_capacity(nums.len());
        let mut result = 0;
        for (i, &num) in nums.iter().enumerate() {
            if num == *max_num {
                max_indexes.push(i);
            }
            let frequency = max_indexes.len();
            if frequency >= k as usize {
                result += max_indexes[max_indexes.len() + -k as usize] + 1
            }
        }
        result as i64
    }
}

fn main() {}
