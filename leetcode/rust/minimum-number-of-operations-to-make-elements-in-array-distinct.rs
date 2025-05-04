// Leetcode problem 3396: Minimum Number of Operations to Make Elements in Array Distinct.

struct Solution {}

impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        let mut table = vec![false; 101];
        for i in (0..=nums.len() - 1).rev() {
            if table[nums[i] as usize] {
                return ((i / 3) + 1) as i32;
            }
            table[nums[i] as usize] = true;
        }
        0
    }
}

fn main() {}
