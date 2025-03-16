// Leetcode problem 2824: Count Pairs Whose Sum is Less than Target.

struct Solution {}

impl Solution {
    pub fn count_pairs(nums: Vec<i32>, target: i32) -> i32 {
        let mut result = 0;
        for i in 0..nums.len() {
            for j in i + 1..nums.len() {
                if nums[i] + nums[j] < target {
                    result += 1;
                }
            }
        }
        result
    }
}

fn main() {}
