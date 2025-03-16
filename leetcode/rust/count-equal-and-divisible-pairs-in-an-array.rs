// Leetcode problem 2176: Count Equal and Divisible Pairs in an Array.

struct Solution {}

impl Solution {
    pub fn count_pairs(nums: Vec<i32>, k: i32) -> i32 {
        let mut result = 0;
        for i in 0..nums.len() {
            for j in i + 1..nums.len() {
                if nums[i] == nums[j] && (i * j) % k as usize == 0 {
                    result += 1;
                }
            }
        }
        result
    }
}

fn main() {}
