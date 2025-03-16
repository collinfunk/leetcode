// Leetcode problem 1980: Find Unique Binary String.

struct Solution {}

impl Solution {
    pub fn find_different_binary_string(nums: Vec<String>) -> String {
        (0..nums.len())
            .map(|x| (nums[x].as_bytes()[x] ^ 1) as char)
            .collect()
    }
}

fn main() {}
