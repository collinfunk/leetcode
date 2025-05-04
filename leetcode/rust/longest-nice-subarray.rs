// Leetcode problem 2401: Longest Nice Subarray.

struct Solution {}

impl Solution {
    pub fn longest_nice_subarray(nums: Vec<i32>) -> i32 {
        let mut used = 0;
        let mut start = 0;
        let mut result = 0;
        for i in 0..nums.len() {
            while used & nums[i] != 0 {
                used ^= nums[start];
                start += 1;
            }
            used |= nums[i];
            result = result.max(i - start + 1);
        }
        result as i32
    }
}

fn main() {}
