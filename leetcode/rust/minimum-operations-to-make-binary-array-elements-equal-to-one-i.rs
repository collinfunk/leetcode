// Leetcode problem 3191: Minimum Operations to Make Binary Array Elements Equal to One I.

struct Solution {}

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut result = 0;
        let mut nums = nums;
        for i in 0..nums.len() - 2 {
            if nums[i] == 0 {
                nums[i] = 1;
                if nums[i + 1] == 0 {
                    nums[i + 1] = 1
                } else {
                    nums[i + 1] = 0
                }
                if nums[i + 2] == 0 {
                    nums[i + 2] = 1
                } else {
                    nums[i + 2] = 0
                }
                result += 1;
            }
        }
        if nums[nums.len() - 2] == 0 || nums[nums.len() - 1] == 0 {
            -1
        } else {
            result
        }
    }
}

fn main() {}
