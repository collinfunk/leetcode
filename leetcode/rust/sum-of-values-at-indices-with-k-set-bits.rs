// Leetcode problem 2859: Sum of Values at Indices With K Set Bits.

struct Solution {}

impl Solution {
    pub fn sum_indices_with_k_set_bits(nums: Vec<i32>, k: i32) -> i32 {
        (0..nums.len())
            .filter(|x| x.count_ones() == k as u32)
            .map(|x| nums[x])
            .sum()
    }
}

fn main() {}
