// Leetcode problem 2966: Divide Array Into Arrays With Max Difference.

struct Solution {}

impl Solution {
    pub fn divide_array(nums: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        let mut nums = nums.clone();
        nums.sort_unstable();
        let mut result = Vec::new();
        for i in (0..nums.len()).step_by(3) {
            if k < nums[i + 2] - nums[i] {
                return Vec::new();
            }
            result.push(vec![nums[i], nums[i + 1], nums[i + 2]]);
        }
        result
    }
}

fn main() {}
