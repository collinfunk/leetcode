// Leetcode problem 747: Largest Number At Least Twice of Others.

struct Solution {}

impl Solution {
    pub fn dominant_index(nums: Vec<i32>) -> i32 {
        let mut sorted_nums = nums.clone();
        sorted_nums.sort_by(|a, b| b.cmp(&a));
        if sorted_nums[0] >= 2 * sorted_nums[1] {
            nums.iter().position(|&x| x == sorted_nums[0]).unwrap() as i32
        } else {
            -1
        }
    }
}

fn main() {}
