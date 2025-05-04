// Leetcode problem 2563: Count the Number of Fair Pairs.

struct Solution {}

impl Solution {
    fn count_pairs(nums: &Vec<i32>, target: i32) -> i64 {
        let mut result = 0;
        let mut left = 0;
        let mut right = nums.len() - 1;
        while left < right {
            if target < nums[left] + nums[right] {
                right -= 1;
            } else {
                result += (right - left) as i64;
                left += 1;
            }
        }
        result
    }

    pub fn count_fair_pairs(nums: Vec<i32>, lower: i32, upper: i32) -> i64 {
        let mut sorted_nums = nums.clone();
        sorted_nums.sort_unstable();
        Self::count_pairs(&sorted_nums, upper) - Self::count_pairs(&sorted_nums, lower - 1)
    }
}

fn main() {}
