// Leetcode problem 896: Monotonic Array.

struct Solution {}

impl Solution {
    pub fn is_monotonic(nums: Vec<i32>) -> bool {
        let mut i = 0;
        while i < nums.len() - 1 && nums[i] == nums[i + 1] {
            i += 1;
        }
        if i < nums.len() - 1 {
            if nums[i] < nums[i + 1] {
                i += 1;
                while i < nums.len() - 1 {
                    if nums[i + 1] < nums[i] {
                        break;
                    }
                    i += 1;
                }
            } else {
                while i < nums.len() - 1 {
                    if nums[i] < nums[i + 1] {
                        break;
                    }
                    i += 1;
                }
            }
        }
        i == nums.len() - 1
    }
}

fn main() {}
